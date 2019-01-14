from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from ..question.models import Question, Like
from .models import User, Friendship
from .forms import EditProfileForm, UserCreateForm
from django.views.generic import UpdateView


# friends page
def get_friends(request):
  current_user = User.objects.get(username=request.user)
  my_friends = Friendship.objects.filter(creator=current_user)
  friends = []
  for friend in my_friends:
    u = User.objects.get(username=friend.friend)
    friends.append(u)
  users = User.objects.all()
  unfriend_users = []
  for u in users:
    if u not in friends:
      unfriend_users.append(u)

  context = {
    'users': unfriend_users,
    'friends': friends,
    'current_user': current_user,
  }
  return render(request, 'accounts/friends.html', context)


# edit user profile
class Edit_profile(UpdateView):
  form_class = EditProfileForm
  template_name = 'accounts/edit_profile.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    users = User.objects.all()
    current_user = User.objects.get(username=self.request.user)
    my_friends = Friendship.objects.filter(creator=current_user)
    friends = []
    for friend in my_friends:
      u = User.objects.get(username=friend.friend)
      friends.append(u)
    unfriend_users = []
    for u in users:
      if u not in friends:
        unfriend_users.append(u)
    context['users'] = unfriend_users
    context['current_user'] = current_user
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
    like = Like.objects.filter(user=request.user, question=question)
    if like:
      likes.append(1)
      like_count += 1
    else:
      likes.append(0)
  mylist = zip(questions, likes)
  current_user = User.objects.get(username=request.user)

  your_friend = False
  friends = Friendship.objects.filter(creator=current_user)
  for ff in friends:
    if ff.friend == user:
      your_friend = True

  flag = True
  if user == current_user:
    flag = False

  context = {
    'your_friend': your_friend,
    'flag': flag,
    'questions': mylist,
    'like_count': like_count,
    'quest_count': quest_count,
    'user': user,
    'current_user': current_user,
  }

  return render(request, 'accounts/profile.html', context)


class Signup(CreateView):
  form_class = UserCreateForm
  success_url = reverse_lazy('accounts:login')
  template_name = 'accounts/signup.html'


def follow(request, pk):
  creator = User.objects.get(username=request.user)
  friend = User.objects.get(pk=pk)
  frindship = Friendship.objects.get_or_create(creator=creator, friend=friend)

  # redirect to the same page user in
  return redirect(request.META.get('HTTP_REFERER'))


def unfollow(request, pk):
  creator = User.objects.get(username=request.user)
  friend = User.objects.get(pk=pk)
  friendship = Friendship.objects.filter(creator=creator, friend=friend)
  friendship.delete()
  return redirect(request.META.get('HTTP_REFERER'))

