from django.shortcuts import render, redirect
from .models import Question, Like
from ..accounts.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import datetime
from django.views.generic import UpdateView
from .forms import QuestionCreateForm, NewQuestionForm, ReAskQuestionForm


def reAsk_question(request, pk):
  question_body = Question.objects.get(id=pk).body,
  if request.method == 'POST':
    question_form = ReAskQuestionForm(request.POST, request.FILES)
    if question_form.is_valid():
      question = question_form.save(commit=False)
      question.sender = request.user
      question.body = question_body[0]
      question.save()
      return HttpResponseRedirect(reverse_lazy('question:home'))
  elif request.method == 'GET':
    form = ReAskQuestionForm()
    current_user = User.objects.get(username=request.user)
    users = User.objects.all()
    context = {
      'form': form,
      'question': question_body[0],
      'user_img': current_user.image,
      'users': users,
    }
    return render(request, 'question/re_ask_quest.html', context)


# ask new question

def add_question(request, pk):
  if request.method == 'POST':
    question_form = NewQuestionForm(request.POST, request.FILES)
    if question_form.is_valid():
      question = question_form.save(commit=False)
      question.sender = User.objects.get(username=request.user)
      question.receiver = User.objects.get(id=pk)
      question.save()
      return HttpResponseRedirect(reverse_lazy('question:add_question', kwargs={'pk': pk}))
  elif request.method == 'GET':
    form = NewQuestionForm()
    current_user = User.objects.get(username=request.user)
    users = User.objects.all()
    context = {
      'form': form,
      'user_img': current_user.image,
      'users': users,
    }
    return render(request, 'question/new_question.html', context)


class AnsQuestion(UpdateView):
  form_class = QuestionCreateForm
  template_name = 'question/ans_quest.html'
  success_url = reverse_lazy('question:quest')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    users = User.objects.all()
    context['users'] = users
    current_user = User.objects.get(username=self.request.user)
    context['user_img'] = current_user.image
    return context

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
    users = User.objects.all()
    current_user = User.objects.get(username=request.user)
    context = {
      'questions': questions,
      'users': users,
      'now': datetime.datetime.now(),
      'user_img': current_user.image,
    }
    return render(request, 'question/question.html', context)
  else:
    return redirect('/')


def home(request):
  if request.user.is_authenticated:
    questions = Question.objects.filter(status=True)
    users = User.objects.all()
    likes = []
    users_images = []
    for question in questions:
      like = Like.objects.filter(user=request.user, question=question)
      user = question.receiver
      question_user = User.objects.filter(username=user)[0]
      users_images.append(question_user)
      if like:
        likes.append(1)
      else:
        likes.append(0)
    mylist = zip(questions, likes, users_images)
    current_user = User.objects.get(username=request.user)
    context = {
      'questions': mylist,
      'users': users,
      'user_img': current_user.image,
    }
    return render(request, 'question/home.html', context)
  else:
    return redirect('/')


def like_question(request, pk):
  user = User.objects.get(username=request.user)
  question = Question.objects.get(id=pk)
  question.likes = question.likes + 1
  like = Like.objects.get_or_create(user=user, question=question, value=True)

  # redirect to the same page user in
  return redirect(request.META.get('HTTP_REFERER'))


def dislike_question(request, pk):
  user = User.objects.get(username=request.user)
  question = Question.objects.get(id=pk)
  question.likes = question.likes - 1
  like = Like.objects.filter(user=user, question=question, value=True)
  like.delete()
  return redirect(request.META.get('HTTP_REFERER'))

