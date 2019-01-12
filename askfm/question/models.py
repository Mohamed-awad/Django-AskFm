from django.db import models
from django.utils import timezone
from ..accounts.models import User


# Question Model
class Question(models.Model):

  sender = models.ForeignKey(User, related_name='senders', on_delete=models.CASCADE)
  body = models.TextField()
  receiver = models.ForeignKey(User, related_name='recievers', on_delete=models.CASCADE)
  answer = models.TextField(default='', blank=True)
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.BooleanField(default=False)
  likes = models.IntegerField(default=0)

  class Meta:
    ordering = ('-updated',)

  def __str__(self):
    return str(self.id)


# Like Model
class Like(models.Model):

  user = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE)
  question = models.ForeignKey(Question, related_name='liked_questions', on_delete=models.CASCADE)
  value = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.user) + ':' + str(self.question) + ':' + str(self.value)
