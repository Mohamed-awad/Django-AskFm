from django.conf.urls import url
from . import views

app_name = 'question'

urlpatterns = [
  url(r'^home$', views.home, name='home'),
  url(r'^ans_quest/(?P<pk>\d+)$', views.AnsQuestion.as_view(), name='Ans_question'),
  url(r'^del/(?P<pk>\d+)$', views.quest_del, name='quest_del'),
  url(r'^question$', views.quest, name='quest'),
  url(r'^like_question/(?P<pk>\d+)/$', views.like_question, name='like_question'),
  url(r'^dislike_question/(?P<pk>\d+)/$', views.dislike_question, name='dislike_question'),
  url(r'^add_question/(?P<pk>\d+)/$', views.add_question, name='add_question'),
  url(r'^re_ask_question/(?P<pk>\d+)/$', views.reAsk_question, name='re_ask_question'),
]
