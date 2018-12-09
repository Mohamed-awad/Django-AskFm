from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Question
from django.contrib.auth.models import User


def home(request):
  list_objects = Question.objects.filter(status=True)
  users = User.objects.filter()
  paginator = Paginator(list_objects, 3)
  page = request.GET.get('page')
  try:
    questions = paginator.page(page)
  except PageNotAnInteger:
    questions = paginator.page(1)
  except EmptyPage:
    questions = paginator.page(paginator.num_pages)
  context = {
    'questions': questions,
    'users': users,
  }
  return render(request, 'question/home.html', context)
