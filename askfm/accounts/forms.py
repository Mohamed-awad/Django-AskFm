from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'image')

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)


class EditProfileForm(forms.ModelForm):
  username = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'image')

  def __init__(self, *args, **kwargs):
    super(EditProfileForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['readonly'] = True

  def clean_email(self):
    email = self.cleaned_data.get('email')
    username = self.cleaned_data.get('username')

    if email and User.objects.filter(email=email).exclude(username=username).count():
      raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
    return email
