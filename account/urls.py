from django.conf.urls import url, include

from account import views, user, group

urlpatterns = [
    url(r'^index/$', user.index, name='index'),
    url(r'^login/$', user.userlogin, name='login'),
    url(r'^logout/$', user.userlogout, name='logout'),
    url(r'^user/', include([
        url(r'^adduser/$', user.adduser, name='adduser'),
        url(r'^deleteuser/$', user.deleteuser, name='deleteuser'),
        url(r'^modify_info/$', user.modify_info, name='modify_info'),
        url(r'^modify_pw/$', user.modify_pw, name='modify_pw'),
    ])),
    url(r'^group/', include([
        url(r'^addgroup/$', group.addgroup, name='addgroup'),
        url(r'^deletegroup/$', group.deletegroup, name='deletegroup'),
        url(r'^intogroup/$', group.intogroup, name='intogroup'),
        url(r'^removegroup/$', group.removegroup, name='removegroup'),
        url(r'^addperm/$', group.addperm, name='addperm'),
        url(r'^deleteperm/$', group.deleteperm, name='deleteperm'),
    ])),
]
