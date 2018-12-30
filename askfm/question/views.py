from django.shortcuts import render, redirect
from .models import Question, Like
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import datetime
from django.views.generic import UpdateView
from .forms import QuestionCreateForm, NewQuestionForm


def add_question(request, pk):
  if request.method == 'POST':
    question_form = NewQuestionForm(request.POST, request.FILES)
    if question_form.is_valid():
      question = question_form.save(commit=False)
      question.sender = request.user
      question.receiver = User.objects.get(id=pk)
      question.save()
      return HttpResponseRedirect(reverse_lazy('question:add_question', kwargs={'pk': pk}))
  elif request.method == 'GET':
    form = NewQuestionForm()
    context = {
      'form': form,
    }
    return render(request, 'question/new_question.html', context)


class AnsQuestion(UpdateView):
  form_class = QuestionCreateForm
  template_name = 'question/ans_quest.html'
  success_url = reverse_lazy('question:quest')

  def get_object(self, queryset=None):
    obj, created = Question.objects.get_or_create(id=self.kwargs['pk'])
    return obj


def quest_del(request, pk):
  question = Question.objects.get(id=pk)
  question.delete()
  return HttpResponseRedirect(reverse_lazy('question:quest'))


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


def like_question(request, pk):
  user = request.user
  question = Question.objects.get(id=pk)
  question.likes = question.likes + 1
  like = Like.objects.get_or_create(user=user, question=question, value=True)
  return HttpResponseRedirect(reverse_lazy('question:home'))


def dislike_question(request, pk):
  user = request.user
  question = Question.objects.get(id=pk)
  question.likes = question.likes - 1
  like = Like.objects.filter(user=user, question=question, value=True)
  like.delete()
  return HttpResponseRedirect(reverse_lazy('question:home'))


