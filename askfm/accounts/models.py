from django.contrib.auth.models import User, PermissionsMixin
from django.db import models


class User(User, PermissionsMixin):
  image = models.ImageField(upload_to='user_images/%Y/%m/%d', blank=True)

  def __str__(self):
    return "{}".format(self.username)


class Friendship(models.Model):
  created = models.DateTimeField(auto_now_add=True, editable=False)
  creator = models.ForeignKey(User, related_name="friendship_creators", on_delete=models.CASCADE)
  friend = models.ForeignKey(User, related_name="friends", on_delete=models.CASCADE)
