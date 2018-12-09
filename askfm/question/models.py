from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Post Model
class Question(models.Model):

  sender = models.ForeignKey(User, related_name='senders', on_delete=models.CASCADE)
  body = models.TextField()
  receiver = models.ForeignKey(User, related_name='recievers', on_delete=models.CASCADE)
  answer = models.TextField()
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.BooleanField(default=False)

  class Meta:
    ordering = ('-publish',)

  def __str__(self):
    return str(self.id)
