from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout #用户认证

from . import forms

from cyweb import settings
from ldap3 import *
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')



class LogoutView(View):

    @login_required
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('account:login'))



class LoginView(View):

    def ldap_check(self, username, password):
        conn = Connection(server=Server(settings.LDAP_URL, port=settings.LDAP_PORT), user=settings.LDAP_PREFIX + username, password=password)
        return conn.bind()

    def ldap_search(self, username):
        conn = Connection(server=Server(settings.LDAP_URL, port=389, get_info=ALL), user=settings.LDAP_PREFIX + 'administrator', password='*9K8fD5', authentication=NTLM, auto_bind=True)
        conn.search(settings.BASE_DN, '(objectCategory=person)', search_scope=SUBTREE, attributes=['sAMAccountName', 'name', 'Mail', 'Sn', 'GivenName'])
        for laap_info in conn.entries:
            if username == laap_info.sAMAccountName:
                return laap_info
        return None

    def get(self, request, *args, **kwargs):
        context = {'form': forms.LoginForm()}
        return render(request, 'login.html', context=context)

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if self.ldap_check(username, password):
                ldap_info = self.ldap_search(username)
                if User.objects.filter(username=username):
                    user = User.objects.get(username=username)
                    user.set_password(password)
                else:
                    user = User.objects.create_user(username=username, password=password)
                user.first_name = ldap_info.GivenName
                user.last_name = ldap_info.Sn
                user.email = ldap_info.Mail
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse('account:index'))
            else:
                context = {'form': forms.LoginForm(), 'info': '用户认证失败'}
                return render(request, 'login.html', context=context)
        else:
            return render(request, 'login.html')