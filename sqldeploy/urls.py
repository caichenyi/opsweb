from django.conf.urls import url, include

from . import forms, db, sql

urlpatterns = [
    url(r'^db/', include([
        url(r'^create/$', db.CreateDBView.as_view(), name='createdb'),
    ])),
    url(r'^sql/', include([
        url(r'^submit/$', sql.SubmitSqlView.as_view(), name='submitsql'),
        url(r'^sqllist/(?P<status>\d+)/$', sql.SqlListView.as_view(), name='sqllist'),
        url(r'^sqldrop/(?P<id>\d+)?(?P<user_id>\d+)/$', sql.SqlDropView.as_view(), name='sqldrop'),
        url(r'^sqlreview/(?P<id>\d+)?(?P<user_id>\d+)/$', sql.SqlReviewView.as_view(), name='sqldrop'),
    ])),
]
