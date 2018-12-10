from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Question
from django.contrib.auth.models import User


def home(request):
  questions = Question.objects.filter(status=True)
  users = User.objects.filter()
  context = {
    'questions': questions,
    'users': users,
  }
  return render(request, 'question/home.html', context)
