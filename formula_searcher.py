from datetime import datetime
from itertools import chain
import math

from django.conf import settings

from ExamPapers.formula_indexer import features_extraction, ino_sem_terms, sort_sem_terms
from ExamPapers.DBManagement.models import *


def formula_retrieval(sorted_sem_terms, k=20):
    #This function retrieves a set of related formulas, which uses the top k retrieval technique
    related_formulas = set()
    if sorted_sem_terms is None:
        return related_formulas
    
    for element in range(len(sorted_sem_terms)):
        for term in sorted_sem_terms[element]:
            try:            
                f_index = formula_index.objects.get(pk=term)
                posting_list  = (f_index.docsids.replace('#', ' ')).split()
        
                formula_objs = formula.objects.filter(pk__in=posting_list, status__exact=True)                                    
                #Convert string to list
                for obj in formula_objs:
                    if obj.status:
                        inorder_temp        = eval(obj.inorder_term)
                        obj.inorder_term    = [term for term in chain.from_iterable(inorder_temp)]
                        
                        sorted_temp         = eval(obj.sorted_term)
                        obj.sorted_term     = sorted_temp[len(sorted_temp)-1]
                        
                        obj.structure_term  = eval(obj.structure_term)
                        obj.constant_term   = eval(obj.constant_term)
                        obj.variable        = eval(obj.variable_term)
                        related_formulas.add(obj)
                                
            except (KeyError, formula_index.DoesNotExist):
                pass
        if len(related_formulas) >= k:
            break
            
    return list(related_formulas)

def is_function(term):
    #"This function checks the type of the term"
    operator_terms = ('lim', 'Lim', 'sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 
                      'cot', 'sec', 'cosec', 'csc', 'log', 'ln', 'lg', 'det', 'gcd', 
                      'lcm', 'min', 'max', 'msqrt', 'mroot')
    return term.endswith(operator_terms)

def sem_matching_score(matching_1gram_sort, unmatching_1gram_sort, 
                       matching_ngram_inorder, unmatching_ngram_inorder, IDF_values, N):
    #This function computes a matching sem_score based on the semantic feature as one formula retrieval
    sem_score = 0
    num_of_func = 0
    #Step 1, 2
    for term in matching_1gram_sort:
        if term in IDF_values:
            sem_score += IDF_values.get(term)
        if is_function(term):
            num_of_func += 1
    
    sem_score += num_of_func*math.log10(N)
    
    #Step 3
    for term in unmatching_1gram_sort:        
        if term in IDF_values:
            sem_score -= IDF_values.get(term)
        
    #Step 4
    for term in matching_ngram_inorder:
        if term in IDF_values:
            sem_score += IDF_values.get(term)
    
    #Additional step
    #for term in unmatching_ngram_inoder:
    #    if term in IDF_values:
    #        sem_score -= IDF_values.get(term)
            
    return sem_score

def struc_matching_score(matching_struc, IDF_values):
    #This function computes a matching score based on the structural feature as one formula retrieval
    struc_score = 0 
    for term in matching_struc:
        if term in IDF_values:
            struc_score += IDF_values.get(term)
    
    return struc_score

def cn_matching_score(matching_cn):
    #This function computes a matching score based on the constant feature as one formula retrieval
    return len(matching_cn)

def var_matching_score(matching_var):
    #This function computes a matching score based on the variable feature as one formula retrieval
    return len(matching_var)

def compute_IDF_values(query_ino_terms, query_sort_terms, query_struc_fea, 
                       related_formulas, N):
    #This funtion computes IDF values of query formula and related formula
    IDF_values = dict()
    #Put term into terms collection
    terms_collection = set(query_ino_terms + query_sort_terms + query_struc_fea)    
        
    for rel_formula in related_formulas:
        terms_collection.update(set(rel_formula.inorder_term + 
                                    rel_formula.sorted_term + 
                                    rel_formula.structure_term))

    #Compute IDF values of query formula and related formula        
    formula_index_obj = formula_index.objects.filter(pk__in=terms_collection)
    for obj in formula_index_obj:
        IDF_values[obj.indexkey]=math.log10(N/obj.df)
        
    return IDF_values

def compute_score(sem_score_norm, struc_score_norm, cn_score_norm, 
                    var_score_norm, a=0.2):
    """This function computes the total of matching score as one formula retrieval
    The parameter a is set to 0.2 which is determined experimentally"""
    
    return ((1-a)*(sem_score_norm+struc_score_norm) + 
            a*(cn_score_norm+var_score_norm))/2
            
def formula_score(query_inoder_ngram, query_sort_1gram, query_struc, query_cn, 
                  query_var, retrie_inoder_ngram, retrie_sort_1gram, retrie_struc, 
                  retrie_cn, retrie_var, IDF_values, N):
    """This function computes the matching score based on four formula features 
    as one formula retrieval"""
    
    #semantic score
    sem_score = sem_matching_score(set(query_sort_1gram)&set(retrie_sort_1gram), 
                       set(retrie_sort_1gram)-set(query_sort_1gram), 
                       set(query_inoder_ngram)&set(retrie_inoder_ngram), 
                       set(retrie_inoder_ngram)-set(query_inoder_ngram), 
                       IDF_values, N)

    #structure score    
    struc_score = struc_matching_score(set(query_struc)&set(retrie_struc), IDF_values)
    
    #constant score
    cn_score = cn_matching_score(set(query_cn)&set(retrie_cn))
    
    #variable score
    var_score = var_matching_score(set(query_var)&set(retrie_var))
    
    return (sem_score, struc_score, cn_score, var_score)

def formulas_ranking(query_ino_terms, query_sort_1gram, query_struc_fea, 
                     query_cn_fea, query_var_fea, related_formulas, IDF_values, N):
    #This function computes the matching score based on four formula features as all formula retrieval. 
    #Then, all the retrieved formulas will be ranked according to their matching scores
    ranked_scores = list()
            
    #Compute the matching score normalization of query formula
    (sem_score_norm, struc_score_norm, cn_score_norm, var_score_norm) = \
        formula_score(query_ino_terms, query_sort_1gram, query_struc_fea, 
                      query_cn_fea, query_var_fea, query_ino_terms, query_sort_1gram, 
                      query_struc_fea, query_cn_fea, query_var_fea, IDF_values, N)    
        
    #Compute the matching scores of related formula    
    for rel_formula in related_formulas:        
        
        (sem_score, struc_score, cn_score, var_score) = \
            formula_score(query_ino_terms, query_sort_1gram, query_struc_fea, 
                          query_cn_fea, query_var_fea, rel_formula.inorder_term, 
                          rel_formula.sorted_term, rel_formula.structure_term, 
                          rel_formula.constant_term, rel_formula.variable_term, 
                          IDF_values, N)
        
        if sem_score_norm != 0:
            sem_score = sem_score/sem_score_norm
        if struc_score_norm != 0:
            struc_score = struc_score/struc_score_norm
        if cn_score_norm != 0:
            cn_score = cn_score/cn_score_norm
        if var_score_norm != 0:
            var_score = var_score/var_score_norm
        score = compute_score(sem_score, struc_score, cn_score, var_score)
        if score > 0:
            ranked_scores.append((rel_formula, score))
    
    #Paging
    results = []
    temp_result = sorted(ranked_scores, key=lambda scores:scores[1], reverse=True)
    for index, (rel_formula, score) in enumerate(temp_result):
        #Question Titles, Topic, Subtopic, 
        #Views, Content, id_show_Question , id_show_Solution , 
        #Question content, All solution, id_Question
        question = rel_formula.question
		#results.append((question.title, question.topic, "[%s]" %question.subtopic,
        #                question.views, rel_formula.formula, index+1, index+2, question.content, 
        #                question.oam_answer_set.all(), rel_formula.question_id))
        
        results.append([rel_formula.question_id, question.topic_id_id, question.content, rel_formula.formula, index+1, index+2, score])
    
    return results, len(temp_result) 

def search_content_formula(mathML):
    "This function retrieves the formulas from a formula input"
    # start_total = datetime.now()
    
    #Extract four types of the formula input
    (query_sem_fea, query_struc_fea, query_cn_fea, query_var_fea) = features_extraction(mathML)
    query_ino_terms = ino_sem_terms(query_sem_fea)
    query_sort_terms = sort_sem_terms(query_sem_fea)

    #end_step1 = datetime.now()
    
    #Related formula retrieval, default k = 20
    #start_step2 = datetime.now()
    related_formulas = formula_retrieval(query_sort_terms)
    #end_step2 = datetime.now()

    query_ino_terms = [term for term in chain.from_iterable(query_ino_terms)]
    query_sort_terms = query_sort_terms[len(query_sort_terms)-1]
        
    #Compute IDF values of all the terms
    #start_step3 = datetime.now()
    N = formula.objects.count()
    
    IDF_values = compute_IDF_values(query_ino_terms, query_sort_terms, 
                                    query_struc_fea, related_formulas, N)
    #end_step3 = datetime.now()
    
    #MO_Formula ranking
    #start_step4 = datetime.now()
    results, num_of_results = formulas_ranking(query_ino_terms, query_sort_terms, query_struc_fea, 
                            query_cn_fea, query_var_fea, related_formulas, 
                            IDF_values, N)
    
    #end_total = datetime.now()

    #print 'features extraction: ' + str(end_step1 - start_total)
    #print 'Related formula retrieval, default k = 20: ' + str(end_step2 - start_step2)
    #print 'Compute IDF values of all the terms: ' + str(end_step3 - start_step3)
    #print 'MO_Formula ranking: ' + str(end_total - start_step4)
    #print 'total: ' + str(end_total - start_total)
    
    return results, num_of_results
    
def search_all_formula(page = 1):
    results = []
    
    formula_obj = formula.objects.filter(status__exact=True)    
    #formula_obj = formula.objects.filter(status__exact=False)                                
                                
    for index, obj in enumerate(formula_obj
                                [(page-1)*10:page*10]):
        question = obj.question
        #Question Titles, Topic, Subtopic
        results.append((obj.question_id, question.topic_id_id, question.content, obj.formula, index+1, index+2, ))

    return results, formula_obj.count()