from django.contrib.auth.models import User, PermissionsMixin
from django.db import models


class User(User, PermissionsMixin):
  image = models.ImageField(upload_to='user_images/%Y/%m/%d', blank=True)

  def __str__(self):
    return "{}".format(self.username)
