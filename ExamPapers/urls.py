from django.conf.urls.defaults import patterns, include, url

import views
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ExamPapers.views.home', name='home'),
    # url(r'^ExamPapers/', include('ExamPapers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/resource/static/image/favicon.ico'}),
	(r'^$',direct_to_template,{'template':'index.html'}),
	(r'^index/$',direct_to_template,{'template':'index.html'}),
	#(r'^search/', direct_to_template,{'template':'search_main.html'}),
	(r'^search/', views.search_page),
	(r'^search_page/', direct_to_template,{'template':'search_main.html'}),
	(r'^search_text/(?P<page_no>\d*)/',views.search_text),
	#(r'^formula/$', views.search_formula),
	#(r'^topics/$',views.topics),
	#(r'^questions/(?P<main_id>\d*)/(?P<sub_id>\d*)/$',views.questions),
	#(r'^statistics/$',views.statistics),
	#(r'^delete/(?P<type>\w*)/(?P<id>\d*)/$',views.delete_record),
	
	#(r'^select_test/$',views.select_paper_topics),
	#(r'^genPaper/(?P<p_sub_id>-?\d*)/(?P<p_topic_id>-?\d*)/(?P<p_subTopic_id>-?\d*)/$',views.gen_paper),
	#(r'^select_question/(?P<main_id>-?\d*)/(?P<sub_id>-?\d*)/$',views.select_questions),
	#(r'^answer_question/(?P<question_ID>-?\d*)/$',views.answer_question),
	#(r'^test_sol_func/$',views.test_solution_checker),

	#basic pages
	(r'^menu/$',direct_to_template,{'template':'menu.html'}),	
	(r'^mathsection/(?P<subj_id>\d*)/$',views.AMaths_Menu),
	(r'^question/(?P<list_type>.*)/(?P<subj_id>\d*)/(?P<page_no>\d*)/$',views.add_math_question),
	(r'^question/$',views.search_page),
	(r'^concept/(?P<subj_id>\d*)/$',views.add_math_concept),
	(r'^concept/(?P<subj_id>\d*)/question/(?P<page_no>\d*)/$',views.add_math_concept_tag),
	(r'^display_addmath_question/(?P<question_id>\d*)/$',views.display_add_math_question),
	
	#Analyzer section
	(r'^analyzer/(?P<subj_id>\d*)/$',views.analyzer_main),
	#url(r'^topic_distribution/(?P<paperset_id>\d*)/$', views.topic_distribution_chart),
	#url(r'^topic_trend/$', views.topic_trend_chart),
	(r'^analyzer/(?P<subj_id>\d*)/paper/tag_cloud/$',views.analyzer_paper_tag),
	(r'^analyzer/(?P<subj_id>\d*)/paper/topic_distribution/$',views.analyzer_paper_topic_distribution),
	(r'^analyzer/(?P<subj_id>\d*)/paper/topic_trend/$',views.analyzer_paper_topic_trend),
	(r'^analyzer/(?P<subj_id>\d*)/paper/concept_distribution/$',views.analyzer_paper_concept_distribution),
	(r'^analyzer/(?P<subj_id>\d*)/paper/concept_trend/$',views.analyzer_paper_concept_trend),
	(r'^analyzer/(?P<subj_id>\d*)/topic/tag_cloud/$',views.analyzer_topic_tag),
	(r'^analyzer_cluster/(?P<subj_id>\d*)/$',views.analyzer_topic_cluster),
	(r'^result_keyword_cluster/(?P<page_no>\d*)/$',views.search_keyword_cluster),
	(r'^result/(?P<page_no>\d*)/$',views.result),
	(r'^result_text/(?P<page_no>\d*)/$',views.result_text),
	(r'^result_keyword/(?P<page_no>\d*)/$',views.result_keyword),
	(r'^result_invertedindex/(?P<page_no>\d*)/$',views.result_invertedindex),
	(r'^result_formula/(?P<page_no>\d*)/$',views.result_formula),
	
	#Admin for Add maths
	(r'^math_admin/(?P<subj_id>\d*)/$',views.AddMaths_Admin),
	(r'^math_admin_list/(?P<list_type>.*)/(?P<subj_id>\d*)/(?P<page_no>\d*)/$',views.AddMaths_Admin_ModifyQuestion),
	(r'^math_admin_form/(?P<list_type>.*)/(?P<page_no>\d*)/(?P<subj_id>\d*)/(?P<list_id>.*)/(?P<question_id>-?\d*)/$',views.AddMaths_Admin_QuestionForm),
	(r'^math_admin_preview/$',views.AddMaths_qPreview),
	(r'^math_admin_modify/(?P<list_type>.*)/(?P<page_no>\d*)/(?P<subj_id>\d*)/$',views.AddMaths_qChange),
	(r'^math_admin_delete/(?P<list_type>.*)/(?P<page_no>\d*)/(?P<subj_id>\d*)/$',views.AddMaths_qDelete),
	(r'^math_admin_taglist/$',views.AddMaths_Admin_TagList),
	(r'^math_admin_regenkeyword/$',views.AddMaths_Admin_RegenKeyword),
	(r'^math_admin_formula/$',views.index),
	(r'^math_admin_tag_delete/$',views.AddMaths_Admin_DeleteTag),
	(r'^math_admin_tag_form/$',views.AddMaths_Admin_TagForm),
	(r'^math_admin_tag_save/$',views.AddMaths_Admin_SaveTag),
	#helper for developers
	(r'^math_admin_missing_sol/$',views.find_missing_sol),
	
	
	(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

)

# This is needed to serve static files like images and css
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

