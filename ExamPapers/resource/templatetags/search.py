from django import template
from ExamPapers.DBManagement.models import *

register = template.Library()

def show_keywords():
	types = ['F','C']
	keywords = [definition.encode("utf8") for definition in tag_definitions.objects.filter(type__in=types).values_list('title', flat=True).order_by('title')]
	return {'show_keywords': keywords}
register.assignment_tag(show_keywords)