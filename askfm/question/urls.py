from django.conf.urls import url
from . import views

app_name = 'question'

urlpatterns = [
  url(r'^home$', views.home, name='home'),
  url(r'^question$', views.quest, name='quest'),
  url(r'^like_question/(?P<pk>\d+)/$', views.like_question, name='like_question'),
  url(r'^dislike_question/(?P<pk>\d+)/$', views.dislike_question, name='dislike_question'),
]
