from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views as core_view

app_name = 'accounts'

urlpatterns = [
  url(r'^login/$', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  url(r'^logout/$', auth_view.LogoutView.as_view(), name='logout'),
  url(r'^signup/$', core_view.Signup.as_view(), name='signup'),
  url(r'^profile/(?P<pk>\d+)$', core_view.my_profile, name='my_profile'),
  url(r'^edit-profile/(?P<pk>\d+)$', core_view.Edit_profile.as_view(), name='edit_profile'),
  url(r'my-friends/$', core_view.get_friends, name='get_friends'),
  url(r'^follow/(?P<pk>\d+)/$', core_view.follow, name='follow'),
  url(r'^unfollow/(?P<pk>\d+)/$', core_view.unfollow, name='unfollow'),
]
