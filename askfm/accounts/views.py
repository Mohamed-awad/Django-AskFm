from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from ..question.models import Question, Like
from .models import User
from .forms import EditProfileForm, UserCreateForm
from django.views.generic import UpdateView


# friends page
def get_friends(request):
  users = User.objects.all()
  current_user = User.objects.get(username=request.user)
  context = {
    'users': users,
    'user_img': current_user.image,
  }
  return render(request, 'accounts/friends.html', context)


# edit user profile
class Edit_profile(UpdateView):
  form_class = EditProfileForm
  template_name = 'accounts/edit_profile.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    users = User.objects.all()
    context['users'] = users
    current_user = User.objects.get(username=self.request.user)
    context['user_img'] = current_user.image
    return context

  def get_success_url(self):
    return reverse_lazy('accounts:my_profile', kwargs={'pk': self.kwargs['pk']})

  def get_object(self, queryset=None):
    obj = User.objects.get(id=self.kwargs['pk'])
    return obj


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
  current_user = User.objects.get(username=request.user)
  context = {
    'questions': mylist,
    'like_count': like_count,
    'quest_count': quest_count,
    'user': user,
    'user_img': current_user.image,
  }

  return render(request, 'accounts/profile.html', context)


class Signup(CreateView):
  form_class = UserCreateForm
  success_url = reverse_lazy('accounts:login')
  template_name = 'accounts/signup.html'

