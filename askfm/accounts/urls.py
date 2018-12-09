from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views as core_view

app_name = 'accounts'

urlpatterns = [
  url(r'^login/$', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  url(r'^logout/$', auth_view.LogoutView.as_view(), name='logout'),
  url(r'^signup/$', core_view.Signup.as_view(), name='signup'),
]
