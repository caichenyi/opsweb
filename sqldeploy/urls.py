from django.conf.urls import url, include

from sqldeploy import views

urlpatterns = [
    url(r'^submit/$', views.submit, name='submit'),
]
