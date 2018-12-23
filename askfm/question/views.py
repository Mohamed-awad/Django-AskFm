from django.shortcuts import render, redirect
from .models import Question, Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import datetime


def quest(request):
  if request.user.is_authenticated:
    questions = Question.objects.filter(receiver=request.user, answer='')
    users = User.objects.filter()
    context = {
      'questions': questions,
      'users': users,
      'now': datetime.datetime.now(),
    }
    return render(request, 'question/question.html', context)
  else:
    return redirect('/')


def home(request):
  if request.user.is_authenticated:
    questions = Question.objects.filter(status=True)
    users = User.objects.filter()
    likes = []
    for question in questions:
      like = Like.objects.filter(user=request.user, question=question)
      if like:
        likes.append(1)
      else:
        likes.append(0)
    mylist = zip(questions, likes)
    context = {
      'questions': mylist,
      'users': users,
    }
    return render(request, 'question/home.html', context)
  else:
    return redirect('/')


@login_required
def like_question(request, pk):
  user = request.user
  question = Question.objects.get(id=pk)
  question.likes = question.likes + 1
  like = Like.objects.get_or_create(user=user, question=question, value=True)
  return HttpResponseRedirect(reverse_lazy('question:home'))


@login_required
def dislike_question(request, pk):
  user = request.user
  question = Question.objects.get(id=pk)
  question.likes = question.likes - 1
  like = Like.objects.filter(user=user, question=question, value=True)
  like.delete()
  return HttpResponseRedirect(reverse_lazy('question:home'))
