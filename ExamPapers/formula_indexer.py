from xml.etree.ElementTree import XML, ElementTree, iterparse
from tempfile import TemporaryFile
import locale
from ExamPapers.DBManagement.models import *
from django.shortcuts import get_object_or_404
from itertools import chain
       
 
def tree_preprocess(dom_tree):
    element = XML(dom_tree)
    
    for e in list(element[0]):
        element.append(e)     
    del element[0]
    
    tempfile = TemporaryFile(suffix='.xml')
    ElementTree(element).write(tempfile)
    tempfile.seek(0)
    return tempfile
    
def features_extraction(dom_tree):
    "This function extracts four types of the formula features from a given DOM tree"
    
    sem_features = list()
    struc_features = list()
    cn_features = set()
    var_features = set()
    stack_node = list()    

    element_tree = tree_preprocess(dom_tree)
    iparse = iterparse(element_tree, ['start','end'])
    #raise Exception({iparse})
    i = 0
    for event, element in iparse:
        i = i+1
        #if i == 3:
		    #raise Exception({element.tag})
        if event == 'start':            
            stack_node.append(element.tag)
        else:
            stack_node.pop()
            
        if event == 'start' and element.tag == 'mo':
            sem_features.append(element.text)            
            if len(stack_node) > 2: #extract structure features
                struc_features += struc_cn_var_extraction(stack_node, element)            
            
        elif event == 'start' and element.tag == 'mi' and element.text == 'e':
            sem_features.append(element.text)
            if len(stack_node) > 2: #extract structure features
                struc_features += struc_cn_var_extraction(stack_node, element)
            
        elif element.tag != 'mrow' and element.tag != 'math' and \
                event == 'start' and element.find('.//mi') is not None:
            sem_features.append(element.tag)
            if len(stack_node) > 2: #extract structure features
                struc_features += struc_cn_var_extraction(stack_node, element)
                            
        #extract constant and variable features
        elif event == 'start' and element.text != 'e': #and len(element.text) == 1:
            if element.tag == 'mn':
                cn_features.add(struc_cn_var_extraction(stack_node, element, True)+'cn')
            elif element.tag == 'mi':
                var_features.add(struc_cn_var_extraction(stack_node, element, True)+'var') 
    
    return (sem_features, struc_features, list(cn_features), list(var_features))

def struc_cn_var_extraction(stack_node, element, cn_var = False):
    """This function extracts three types of the formula features
    such as structural, constant and variable"""
    nodes = ''
    if cn_var:
        for node in stack_node[1:len(stack_node)-1]:
            nodes += node + '$'
        return nodes         
    else:
        for node in stack_node[1:len(stack_node)-1]:
            nodes += node + '$'
        if element.text is None:
            nodes += element.tag
        else:
            nodes += element.text
        return [nodes]

def ino_sem_terms(sem_features):
    "This function generates the in-order semantic terms"
    terms = list()
    if len(sem_features) <= 0:
        return terms

    #4-gram
    terms = [[sem_features[i] + '$' + sem_features[i+1] + '$' + sem_features[i+2] 
              + '$' + sem_features[i+3] for i in range(len(sem_features)-3)]]

    #3-gram
    terms += [[sem_features[i] + '$' + sem_features[i+1] + '$' + sem_features[i+2] 
              for i in range(len(sem_features)-2)]]
        
    #2-gram
    terms += [[sem_features[i] + '$' + sem_features[i+1] 
             for i in range(len(sem_features)-1)]]
                                    
    return terms

def sort_sem_terms(sem_features):
    "This function generates the sorted semantic terms"
    terms = list()
    if len(sem_features) <= 0:
        return terms
    locale.setlocale(locale.LC_ALL, (''))
    sem_features.sort(cmp=locale.strcoll)

    #4-gram
    terms = [[sem_features[i] + '$' + sem_features[i+1] + '$' + sem_features[i+2] 
             + '$' + sem_features[i+3] for i in range(len(sem_features)-3)]]

    #3-gram
    terms += [[sem_features[i] + '$' + sem_features[i+1] + '$' 
              + sem_features[i+2] for i in range(len(sem_features)-2)]]
    
    #2-gram
    terms += [[sem_features[i] + '$' + sem_features[i+1] 
              for i in range(len(sem_features)-1)]]
    
    #1-gram
    terms += [[sem_features[i] for i in range(len(sem_features))]]            
        
    return terms

def insert_posting_list(posting_list, start, end, docid):
    "This function inserts a docid into the posting list"
    temp = (start+end)/2
    if start == temp:
        if long(posting_list[start]) > docid:
            posting_list.insert(start, docid)
        elif long(posting_list[start]) < docid < long(posting_list[end]):
            posting_list.insert(end,docid)
        elif long(posting_list[end]) < docid:
            posting_list.append(docid)
        else:
            return False
    else:        
        if long(posting_list[temp]) > docid:
            return insert_posting_list(posting_list, start, temp, docid)
        elif long(posting_list[temp]) < docid:
            return insert_posting_list(posting_list, temp, end, docid)
        else:
            return False

    return True

def create_formula_index(indexid, term):
    try:
        f_index = formula_index.objects.get(pk=term)
        posting_list = (f_index.docsids.replace('#', ' ')).split()
        #A term can appear in one formula twice
        if insert_posting_list(posting_list, 0, len(posting_list)-1, indexid):
            temp = ''
            for item in posting_list:
                temp += '#' + str(item) + '#' 
            f_index.docsids = temp
            f_index.df = len(posting_list)               
    except (KeyError, formula_index.DoesNotExist):
        f_index = formula_index(term, '#'+str(indexid)+'#', 1)
    
    f_index.save()

def create_index_model(formula_input, mathML, id):
    "This function creates the index model in database"
    try:
        formula_obj = get_object_or_404(formula, pk=id)
        
		#if formula_obj.status == 'Y':
        if formula_obj.status == 0:
            #Extract four types of formula_obj
            (sem_feas, struc_feas, cn_feas, var_feas) = features_extraction(mathML)            
            
            # Generate index terms
            inorder_sem_terms = ino_sem_terms(sem_feas)
            sorted_sem_terms = sort_sem_terms(sem_feas)
            
            #Insert into formulas table
            formula_obj.inorder_term = inorder_sem_terms
            formula_obj.sorted_term = sorted_sem_terms
            formula_obj.structure_term = struc_feas
            formula_obj.constant_term = cn_feas
            formula_obj.variable_term = var_feas
            formula_obj.status = 1
            formula_obj.save()
            
            #Create index term in formula_index table
            for term in chain.from_iterable(inorder_sem_terms + sorted_sem_terms):
                create_formula_index(formula_obj.indexid, term)
                
            for term in chain(struc_feas, cn_feas, var_feas):            
                create_formula_index(formula_obj.indexid, term)
                                                      
    except (KeyError, formula.DoesNotExist):
        print "Error"
        
    while id <= formula.objects.count():
        try:
            formula_obj = formula.objects.get(pk=id+1)
            return formula_obj.indexid
        except (KeyError, formula.DoesNotExist):
            id += 1
    