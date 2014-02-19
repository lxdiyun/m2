from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from ExamPapers.DBManagement.models import *

#for calling java at version 2
import urllib2
import urllib

import re

#set java server Java Server
java_server='http://live.2.dev2012oexpp.appspot.com'
#java_server='http://127.0.0.1:8888'

#_____________________________________________#
def myExample(request):
	return simplejson.dumps({'message':'Hello World'})

dajaxice_functions.register(myExample)

#_____________________________________________#
def getSolution(request,q_id):
	params={}
	
	q=question.objects.get(id=q_id)
	if(q.std_answer!=None and q.std_answer!=''):
		params['answer']=q.std_answer		
	elif(q.std_answer_latex!=None and q.std_answer_latex!=''):
		params['answer']=q.std_answer_latex
	else:
		ans=answer.objects.filter(question_id=q_id)
		if (len(ans)>0):
			params['answer']=ans[0].content
		else:
			params['answer']='No Solution Found'
	
	return simplejson.dumps(params)

dajaxice_functions.register(getSolution)

#_____________________________________________#
#test function
def check_solution(request,user_input,actual_ans):
	param={}
	
	javaParam=urllib.urlencode({"userans":user_input,"actualans":actual_ans})
	param['result'] = urllib2.urlopen(java_server+"/solchk",javaParam).read()
	
	return simplejson.dumps(param)
	
dajaxice_functions.register(check_solution)

#test function
def check_conversion(request,user_input):
	param={}
	param['result'] = latex2asciiMathml(user_input)
	return simplejson.dumps(param)
	
dajaxice_functions.register(check_conversion)

#_____________________________________________#
def add_math_chkSol(request,user_input,question_id,part):
	param={}
	#add code to preprocess the inputs here		
	
	ans=question.objects.get(id=question_id).type_answer
	whole_ans=ans	#for checking
	ans=ans.split(';')
	qtype=question.objects.get(id=question_id).type
	if(qtype==None):
		qtype=''
	else:
		qtype=qtype.split(';')[part][0]
	if(ans[part].strip(' ')==''):
		param['result']='No standard answer'
	else:
		if(check(user_input,ans[part],qtype)):
			param['result']='The answer is correct'
		else:
			param['result']='The answer is wrong'
			
	
	#for checking
	param['result'] = param['result']+"\nYour Ans: "+user_input+" \nActual Ans(whole): "+whole_ans
	param['result'] = param['result']+"\nconverted: "+latex2asciiMathml(user_input)
	param['result'] = param['result'] + " \npart   : "+ans[part]
	param['result'] = param['result'] + " \ntype   : _"+qtype+"_"
			
	#javaParam=urllib.urlencode({"userans":user_input,"actualans":ans})
	#param['result'] = urllib2.urlopen(java_server+"/solchk",javaParam).read()
	
	return simplejson.dumps(param)
	
dajaxice_functions.register(add_math_chkSol)

#_____________________________________________#
#helper method to convert latex to asciiMathml (functions MUST comform to {})
def latex2asciiMathml(value):
	
	#step1: remove all white spaces
	val=value
	val=re.sub(r'\s', '', val)
	val=re.sub(r'^\\\[', '', val)
	val=re.sub(r'\\\]$', '', val)
	val=re.sub(r'^\$\$', '', val)
	val=re.sub(r'\$\$$', '', val)
	
	#step2: replace functions
	
	#2: fractions
	eq_start=val.find("\\frac")	
	while(eq_start>-1):
		temp=val[:eq_start]+"("
		end=eq_start+5
		for i in range(0,2):			
			if(val[end]!='{'):
				return "Error in \\frac at "+str(end)+" require {"
			end=end+1
			start=end
			opCount=1	#set end and opCount as confirm is '{'
			while(val[end]!='}'or opCount!=0):
				end=end+1
				if (val[end]=='{'):
					opCount=opCount+1
				elif (val[end]=='}'):
					opCount=opCount-1
			temp=temp+"("+val[start:end]+")/"
			end=end+1 #start next{}
		temp=temp.rstrip('/')+")"+val[end:]
		val=temp
		eq_start=val.find("\\frac")
		
	#2: square root special case
	eq_start=val.find("\\sqrt[")
	while(eq_start>=0):
		temp=val[:eq_start]+"(root("
		#obtain root
		end=eq_start+5
		opCount=1
		while(val[end]!=']'or opCount!=0):
			end=end+1
			if (val[end]=='['):
				opCount=opCount+1
			elif (val[end]==']'):
				opCount=opCount-1
		temp=temp+val[eq_start+6:end]+")("
		#obtain value
		eq_start=end+1
		end=eq_start
		opCount=1
		while(val[end]!='}'or opCount!=0):
			end=end+1
			if (val[end]=='{'):
				opCount=opCount+1
			elif (val[end]=='}'):
				opCount=opCount-1
		temp=temp+val[eq_start+1:end]+"))"+val[end+1:]
		#store results and check for another instance
		val=temp
		eq_start=val.find("\\sqrt[")
		
	#for general functions
	patt=[]
	patt.append({'pre':"\\overrightarrow",'post':'(vec','end':')'})
	patt.append({'pre':"\\underline",'post':'(ul','end':')'})
	patt.append({'pre':"\\overline",'post':'(bar','end':')'})
	patt.append({'pre':"\\mathrm",'post':' mbox','end':' '})
	patt.append({'pre':"\\sqrt",'post':'(sqrt','end':')'})
	patt.append({'pre':"\\ddot",'post':'(ddot','end':')'})
	patt.append({'pre':"\\vec",'post':'(vec','end':')'})	
	patt.append({'pre':"\\bar",'post':'(bar','end':')'})	
	patt.append({'pre':"\\hat",'post':'(hat','end':')'})	
	patt.append({'pre':"\\dot",'post':'(dot','end':')'})	
	patt.append({'pre':"^",'post':"^",'end':''})
	patt.append({'pre':"_",'post':'_','end':''})				
	
	for p in patt:
		eq_start=val.find(p['pre']+"{")
		while(eq_start>=0):
			temp=val[:eq_start]+p['post']
			end=eq_start				
			opCount=0
			start=-1
			while(val[end]!='}'or opCount!=0):
				end=end+1
				if (val[end]=='{'):
					opCount=opCount+1
					if(start==-1):
						start=end
				elif (val[end]=='}'):
					opCount=opCount-1
			temp=temp+"("+val[start+1:end]+")"+p['end']+val[end+1:]
			val=temp
			eq_start=val.find(p['pre']+"{")		
			
			
	#step3: replace symbols (and enclose in bracket to represent a unit)
	val=val.replace('\\varepsilon',' varepsilon ')
	val=val.replace('\\bigtriangledown',' grad ')
	val=val.replace('\\Leftrightarrow',' fArr ')
	val=val.replace('\\leftrightarrow',' harr ')	
	val=val.replace('\\diamond',' diamond ')
	val=val.replace('\\epsilon',' epsilon ')	
	val=val.replace('\\upsilon',' upsilon ')
	val=val.replace('\\rightarrow',' rarr ')
	val=val.replace('\\Rightarrow',' rArr ')
	val=val.replace('\\leftarrow',' larr ')
	val=val.replace('\\Leftarrow',' lArr ')	
	val=val.replace('\\downarrow',' darr ')	
	val=val.replace('\\setminus',' \\\\ ')
	val=val.replace('\\Lambda',' Lambda ')
	val=val.replace('\\lambda',' lambda ')	
	val=val.replace('\\subseteq',' sube ')	
	val=val.replace('\\supseteq',' supe ')
	val=val.replace('\\parallel',' |\\| ')			
	val=val.replace('\\bigwedge',' ^^^ ')	
	val=val.replace('\\superset',' sup ')
	val=val.replace('\\uparrow',' uarr ')
	val=val.replace('\\bigotimes',' ox ')
	val=val.replace('\\propto',' prop ')	
	val=val.replace('\\bigoplus',' o+ ')
	val=val.replace('\\Sigma',' Sigma ')
	val=val.replace('\\Gamma',' Gamma ')
	val=val.replace('\\omega',' omega ')
	val=val.replace('\\alpha',' alpha ')	
	val=val.replace('\\gamma',' gamma ')	
	val=val.replace('\\theta',' theta ')
	val=val.replace('\\sigma',' sigma ')
	val=val.replace('\\Delta',' Delta ')
	val=val.replace('\\Omega',' Omega ')
	val=val.replace('\\Theta',' Theta ')
	val=val.replace('\\lfloor',' |__ ')
	val=val.replace('\\rfloor',' __| ')		
	val=val.replace('\\bigodot',' o. ')
	val=val.replace('\\models',' |== ')
	val=val.replace('\\subset',' sub ')
	val=val.replace('\\nabla',' grad ')	
	val=val.replace('\\bigcap',' nnn ')
	val=val.replace('\\bigcup',' uuu ')
	val=val.replace('\\bigvee',' vvv ')
	val=val.replace('\\mapsto',' |->')	
	val=val.replace('\\sinh',' sinh ')
	val=val.replace('\\cosh',' cosh ')
	val=val.replace('\\tanh',' tanh ')	
	val=val.replace('\\forall',' AA ')	
	val=val.replace('\\prod',' prod ')	
	val=val.replace('\\oint',' oint ')	
	val=val.replace('\\otimes',' ox ')
	val=val.replace('\\beta',' beta ')	
	val=val.replace('\\zeta',' zeta ')		
	val=val.replace('\\vdash',' |-- ')	
	val=val.replace('\\approx',' ~~ ')
	val=val.replace('\\|',' |\\\\| ')
	val=val.replace('\\lceil',' |~ ')
	val=val.replace('\\rceil',' ~| ')	
	val=val.replace('\\perp',' _|_ ')
	val=val.replace('\\equiv',' -= ')
	val=val.replace('\\oplus',' o+ ')
	val=val.replace('\\wedge',' ^^ ')
	val=val.replace('\\times',' xx ')	
	val=val.replace('\\infty',' oo ')	
	val=val.replace('\\neg',' not ')
	val=val.replace('\\sum',' sum ')
	val=val.replace('\\odot',' o. ')
	val=val.replace('\\Phi',' Phi ')
	val=val.replace('\\Psi',' Psi ')
	val=val.replace('\\tau',' tau ')
	val=val.replace('\\rho',' rho ')
	val=val.replace('\\phi',' phi ')
	val=val.replace('\\eta',' eta ')
	val=val.replace('\\prec',' -< ')
	val=val.replace('\\int',' int ')
	val=val.replace('\\cong',' ~= ')
	val=val.replace('\\sin',' sin ')
	val=val.replace('\\cos',' cos ')
	val=val.replace('\\tan',' tan ')
	val=val.replace('\\csc',' csc ')
	val=val.replace('\\sec',' sec ')
	val=val.replace('\\cot',' cot ')
	val=val.replace('\\log',' log ')	
	val=val.replace('\\det',' det ')
	val=val.replace('\\dim',' dim ')
	val=val.replace('\\lim',' lim ')
	val=val.replace('\\gcd',' gcd ')
	val=val.replace('\\min',' min ')
	val=val.replace('\\max',' max ')	
	val=val.replace('\\leq',' <= ')
	val=val.replace('\\geq',' >= ')	
	val=val.replace('\\ast',' ** ')
	val=val.replace('\\cap',' nn ')
	val=val.replace('\\cup',' uu ')
	val=val.replace('\\vee',' vv ')
	val=val.replace('\\div',' -: ')
	val=val.replace('\\circ',' @ ')
	val=val.replace('\\succ',' > ')	
	val=val.replace('\\neq',' != ')			
	val=val.replace('\\mu',' mu ')
	val=val.replace('\\pi',' pi ')							
	val=val.replace('\\nu',' nu ')		
	val=val.replace('\\xi',' xi ')					
	val=val.replace('\\Xi',' Xi ')		
	val=val.replace('\\Pi',' Pi ')	
	val=val.replace('\\pm',' +- ')
	val=val.replace('\\in',' in ')
	val=val.replace('\\ln',' ln ')	
	val=val.replace('\\notin',' !in ')	
					
	#val=val.replace('','')
		
	return val
	
#helper method to check maths values	
def check_value(input,ans):
	converted=latex2asciiMathml(input)
	#not is to for itemsets: example A'nnB
	javaParam=urllib.urlencode({"userans":converted.replace("'","(not)"),"actualans":ans.replace("'","(not)")})	
	result = urllib2.urlopen(java_server+"/solchk",javaParam).read()
	
	if(result=='True'):
		return True
	return False 

def check_ratio(input_a,input_b,ans):
	conv_a=latex2asciiMathml(input_a)
	conv_b=latex2asciiMathml(input_b)
	converted=conv_a+"/"+conv_b
	javaParam=urllib.urlencode({"userans":converted,"actualans":ans})	
	result = urllib2.urlopen(java_server+"/solchk",javaParam).read()
	# only accept x:y where question is ratio of x to y
	if(result=='True'):
		return True
	return False 

#for coord, matrix and range
def check_multi(input,ans):
	#input and ans are arrays
	result=True
	for i in range(0,len(input)):
		result=result and check_value(input[i],ans[i])
	return result

#for multiple range
def check_mRange(input,ans):
	if(len(input)!=len(ans)):
		return False
		
	l=len(input)/2
	match=True
	sol=ans
	for x in range(0,l):
		inner_match=False
		val=[input[2*x],input[1+2*x]]
		y=x
		while(inner_match!=True and y<l):
			#switch
			sw1=sol[2*y]
			sw2=sol[1+2*y]
			sol[2*y]=sol[2*x]
			sol[1+2*y]=sol[1+2*x]
			sol[2*x]=sw1
			sol[1+2*x]=sw2
			#endswitch
			chk=[sol[2*x],sol[1+2*x]]
			inner_match=inner_match or check_multi(val,chk)
			if(inner_match!=True):
				y=y+1
		match=match and inner_match
		if(match==False):
			return False
	return match
				

#need to shift the special cases to check_multi				
def check(input,ans,type):	
	input_list=input.strip(' ').split(';')
	ans_list=ans.strip(' ').split('|')			
	#special cases
	if(type=='r'):	#type ratio
		return check_ratio(input_list[0],input_list[1],ans_list[0])	
	if(type=='i'):		
		for i in range(0,len(input_list)):
			if (input_list[i]==None or input_list[i].strip(' ')==''):
				input_list[i]='$$\\infty$$'	
		if(len(input_list)>2):
			return check_mRange(input_list,ans_list)
	#type coord,matrix,range,value		
	return check_multi(input_list,ans_list)
	