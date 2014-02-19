from haystack import indexes
from ExamPapers.DBManagement.models import *

class questionIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	content = indexes.CharField(model_attr='content')
	paper_id = indexes.CharField(model_attr='paper_id')
	question_no = indexes.IntegerField(model_attr='question_no')
	topic_id = indexes.CharField(model_attr='topic_id')
	subtopic_id = indexes.CharField(model_attr='subtopic_id')
	marks = indexes.IntegerField(model_attr='marks')
	question_id = indexes.CharField(model_attr='id')
	#topic_id = CharField(model_attr='topic_id')
	def get_model(self):
		return question
		
	def index_queryset(self, using=None):
		return self.get_model().objects.all()