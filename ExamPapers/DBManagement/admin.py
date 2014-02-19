from django.contrib import admin
import models

class DefaultAdmin(admin.ModelAdmin):  
	pass
admin.site.register(models.education_level, DefaultAdmin)
admin.site.register(models.paperset, DefaultAdmin)
admin.site.register(models.subject, DefaultAdmin)
admin.site.register(models.topic, DefaultAdmin)
admin.site.register(models.subtopic, DefaultAdmin)
admin.site.register(models.tag, DefaultAdmin)
admin.site.register(models.tag_definitions, DefaultAdmin)
#admin.site.register(models.keyword, DefaultAdmin)

""" this section is not needed
admin.site.register(models.subquestion, DefaultAdmin)
admin.site.register(models.resource, DefaultAdmin)
admin.site.register(models.user, DefaultAdmin)
admin.site.register(models.UserAbility, DefaultAdmin)
admin.site.register(models.SubjectAbility, DefaultAdmin)
admin.site.register(models.TopicAbility, DefaultAdmin)
admin.site.register(models.Test, DefaultAdmin)
admin.site.register(models.Testquestion, DefaultAdmin)
admin.site.register(models.TopicDescription, DefaultAdmin)
admin.site.register(models.Feedback, DefaultAdmin)
"""

class QuestionAdmin(admin.ModelAdmin):
	list_display=('id','content')
	list_filter=('topic_id','paper_id')
	
admin.site.register(models.question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
	list_display=('id','content')
	list_filter=('question_id',)
admin.site.register(models.answer, AnswerAdmin)

class PaperAdmin(admin.ModelAdmin):
	list_display=('id','year','month','number')
	
admin.site.register(models.paper, PaperAdmin)
	
class ImageAdmin(admin.ModelAdmin):
	list_display=('id','imagepath')
	
admin.site.register(models.image, ImageAdmin)

