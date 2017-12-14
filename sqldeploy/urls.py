from django.conf.urls import url, include

from sqldeploy import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]
