from django.db import models

#Education Level - Eg. O'Level, A'Level, etc.
class education_level(models.Model):
	id = models.IntegerField(primary_key=True, null=False)
	title = models.CharField(max_length=64,null=True)
	description = models.CharField(max_length=1000,null=True)
	
	def __str__(self):
		return str(self.title)

#edu_level:
#01: undergrad
#02: O'Level
class subject(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	title = models.TextField('title',null=True)
	edu_level_id = models.ForeignKey(education_level,null=True)
	
	def __str__(self):
		return str(self.title)

class topic(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	subject_id = models.ForeignKey(subject,null=True)
	title = models.TextField('title',null=True)
	kvalue = models.IntegerField('kvalue',null=True)
	
	def __str__(self):
		return str(self.title)
	
class subtopic(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	topic_id = models.ForeignKey(topic,null=True)
	title = models.TextField('title',null=True)
	
	def __str__(self):
		return str(self.title)

class paperset(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	title = models.TextField('title',null=True)
	subject_id = models.ForeignKey(subject,null=False)
	
	def __str__(self):
		return str(self.title)

#topic_id if null will represent a paper covering all topics
#topic_id and subject_id describes paper and does not confine the questions
class paper(models.Model):
	id = models.CharField(max_length=64,primary_key=True, null=False)
	year = models.TextField('year',null=True)
	month = models.TextField('month',null=True)
	number = models.IntegerField('number',null=True)
	subject_id = models.ForeignKey(subject,null=False)
	paperset_id = models.ForeignKey(paperset,null=False)
	
	def __str__(self):
		return str(self.id)
	
class question(models.Model):
	id = models.CharField(max_length=64, primary_key=True,null=False)
	paper_id = models.ForeignKey(paper,null=True)
	question_no = models.SmallIntegerField('question_no',max_length=6,null=True)
	content = models.TextField('content',null=False)
	topic_id = models.ForeignKey(topic,null=True)
	subtopic_id = models.ForeignKey(subtopic,null=True)
	std_answer = models.CharField(max_length=128,null=True)
	marks = models.IntegerField('marks',max_length=2,null=True)
	input = models.CharField(max_length=512,null=True,default=None)
	type_answer = models.CharField(max_length=512,null=True)
	type = models.CharField(max_length=512,null=True,default=None)
	
	def __str__(self):
		return str(self.id)

class answer(models.Model):
	id = models.AutoField('id',primary_key=True,null=False)
	question_id = models.ForeignKey(question,null=False)
	content = models.TextField('content',null=False)
	
	def __str__(self):
		return str(self.id)
	
class image(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	qa = models.TextField('qa',null=True)
	qa_id = models.CharField('qa_id',max_length=64,null=False)
	imagepath = models.TextField('imagepath',null=False)
	
	def __str__(self):
		return str(self.id)

class formula(models.Model):
    #indexid = models.PositiveIntegerField(primary_key=True)
    indexid = models.AutoField('index ID', primary_key=True)
    question = models.ForeignKey(question)
    formula = models.CharField(max_length=1024, null=True, blank=True)
    status = models.BooleanField(default=True)
    inorder_term = models.CharField(max_length=1024, null=True, blank=True)
    sorted_term = models.CharField(max_length=1024, null=True, blank=True)
    structure_term = models.CharField(max_length=1024, null=True, blank=True)
    constant_term = models.CharField(max_length=1024, null=True, blank=True)
    variable_term = models.CharField(max_length=1024, null=True, blank=True)
            
    def __unicode__(self):
        return self.formula

class formula_index(models.Model):
    indexkey = models.CharField('index key', primary_key=True, max_length=64)
    docsids = models.CharField(max_length=9192, null=True, blank=True)
    df = models.PositiveIntegerField('frequency', default=1, blank=True)
		
#Classes for Clustering
'''class keyword(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	key = models.TextField('key',null=True)
	subject_id = models.ForeignKey(subject,null=False)
	
	def __str__(self):
		return str(self.id)'''

#Classes for Tags
class tag_definitions(models.Model):
	id = models.AutoField('id',primary_key=True,null=False)
	title = models.TextField('title',null=True)
	type = models.CharField('type', max_length=1)
	topic = models.ForeignKey(topic, null=True)
	content = models.TextField('content',null=True)
	
	def __str__(self):
		return str(self.id)

class tag(models.Model):
	id = models.AutoField('id',primary_key=True,null=False)
	question_id = models.ForeignKey(question,null=False, related_name='tags')
	tag = models.ForeignKey(tag_definitions,null=False)
	
	def __str__(self):
		return str(self.id)
	
""" This line onwards doesnt concern data analysis, therefore commented out
#identify using qid and question_part
class subquestion(models.Model):
	qid = models.ForeignKey(question,null=True)
	question_no = models.SmallIntegerField('question_no',max_length=6,null=True)
	#question_part = models.SmallIntegerField('question_no',max_length=6,null=True)
	question_part = models.CharField('question_no',max_length=6,null=True)
	marks = models.CharField(max_length=16,null=True)
	content = models.TextField('content',null=False)
	std_answer = models.CharField(max_length=128,null=True)
	
	def __str__(self):
		return str(self.content)
		
class resource(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	subject_id = models.ForeignKey(subject,null=True)
	content = models.TextField('content',null=True)
	doc_path = models.TextField('doc_path',null=True)
	time = models.DateTimeField(auto_now=False)
	user_id = models.IntegerField('user_id',null=True)
	topic_id = models.ForeignKey(topic,null=True)
	subtopic_id = models.ForeignKey(subtopic,null=True)
	category = models.TextField('category',null=True)
	
	def __str__(self):
		return str(self.id)
	
class user(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	name = models.TextField('name',null=True)
	photo = models.TextField('photo',null=True)
	email = models.EmailField(max_length=75,null=True)
	points = models.IntegerField('points',null=True)
	time_reg = models.TimeField(auto_now=False,null=True)
	time_login = models.TimeField(auto_now=False,null=True)
	status = models.TextField('status',null=True)
	role = models.TextField('role',null=True)
	subject = models.TextField('subject',null=True)
	dob = models.DateField(auto_now=False,null=True)
	gender = models.TextField('gender',null=True)
	country = models.TextField('country',null=True)
	city = models.TextField('city',null=True)
	school = models.TextField('school',null=True)
	
	def __str__(self):
		return str(self.id)
	
class UserAbility(models.Model):
	user_id = models.ForeignKey(user,null=False)
	subject_abilityid = models.IntegerField('subject ability',null=False)
	topic_abilityid = models.IntegerField('topic ability',null=False)
	
class SubjectAbility(models.Model):
	subject_id = models.IntegerField('subject_id',primary_key=True,null=False)
	ability_id = models.IntegerField('ability_id',null=False)
	level = models.DecimalField(max_digits=5,decimal_places=4,null=False)
	
	def __str__(self):
		return str(self.subject_id)
	
  
class TopicAbility(models.Model):
	topic_id = models.IntegerField('topic_id',primary_key=True,null=False)
	ability_id = models.IntegerField('ability_id',null=False)
	level = models.DecimalField(max_digits=5,decimal_places=4,null=False)
	
	def __str__(self):
		return str(self.topic_id)
	

class Test(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	test_type = models.TextField('test_type',null=False)
	user_id = models.ForeignKey(user,null=True)
	subject_id = models.ForeignKey(subject,null=True)
	topic_id = models.ForeignKey(topic,null=True)
	status = models.CharField(max_length=1,null=True)
	date = models.DateField(auto_now=False,null=False)
	time = models.TimeField(auto_now=False,null=False)
	score = models.DecimalField(max_digits=5,decimal_places=4,null=True)
	
	def __str__(self):
		return str(self.id)
	
	
class Testquestion(models.Model):
	test_id = models.ForeignKey(Test,null=True)
	question_no = models.IntegerField('question_no',max_length=10,null=False) 
	question_id = models.ForeignKey(question,null=True)
	user_answer = models.CharField(max_length=64,null=True)
	correctness = models.IntegerField('correctness',max_length=10,null=True)
	
	
class TopicDescription(models.Model):
	topic_id = models.ForeignKey(topic,null=False)
	summary = models.TextField('summary',null=True)
	
	
class Feedback(models.Model):
	id = models.IntegerField('id',primary_key=True,null=False)
	#name = models.TextField('name')
	user_id = models.IntegerField('user_id',null=True)
	#email = models.EmailField(null=False)
	title = models.TextField('title',null=False)
	comment = models.TextField('comment',null=False)
	time = models.TimeField(auto_now=False,null=False)
	status = models.TextField('status',null=False)
	
	def __str__(self):
		return str(self.title) + self.comment
"""							  