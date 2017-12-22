from django.conf.urls import url, include
from . import views, user

urlpatterns = [
    url(r'^index/$', user.index, name='index'),
    url(r'^login/$', user.LoginView.as_view(), name='login'),
    url(r'^logout/$', user.LogoutView.as_view(), name='logout'),
]