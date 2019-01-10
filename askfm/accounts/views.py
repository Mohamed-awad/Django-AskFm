from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from askfm.question.models import Question, Like
from django.contrib.auth.models import User


def my_profile(request, pk):
  user = User.objects.filter(id=pk)[0]
  questions = Question.objects.filter(status=True, receiver=user)
  likes = []
  like_count = 0
  quest_count = len(questions)
  for question in questions:
    like = Like.objects.filter(user=user, question=question)
    if like:
      likes.append(1)
      like_count += 1
    else:
      likes.append(0)
  mylist = zip(questions, likes)
  context = {
    'questions': mylist,
    'like_count': like_count,
    'quest_count': quest_count,
    'user': user,
  }

  return render(request, 'accounts/profile.html', context)


class Signup(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('accounts:login')
  template_name = 'accounts/signup.html'



