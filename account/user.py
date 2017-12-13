from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout #用户认证
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from ldap3 import *
from opsweb import settings


@login_required
def index(request):
    return render(request, 'index.html')


def userlogin(request):
    if request.method == "GET":
        return render(request, 'account/user/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        conn = Connection(server=Server(settings.LDAP_URL, port=settings.LDAP_PORT), user=settings.LDAP_PREFIX + username, password=password)
        if conn.bind():
            if not User.objects.filter(username=username):
                user = User.objects.create_user(username=username, password=password)
            else:
                user = User.objects.get(username=username)
                user.set_password(password)
            conn.search(settings.BASE_DN, '(objectCategory=person)', search_scope=SUBTREE, attributes=['sAMAccountName', 'name', 'mail', 'manager', 'Sn', 'GivenName'])
            for i in conn.entries:
                if username == i.sAMAccountName:
                    user.first_name = i.GivenName
                    user.last_name = i.Sn
                    user.email = i.Mail
                    break
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('account:index'))
        else:
            context = {'info': '╭∩╮  认证失败  ╭∩╮'}
            return render(request, 'account/user/login.html', context)


@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login'))


@permission_required('account.user_manage')
@login_required
def deleteuser(request):
    if request.method == "GET":
        return render(request, 'account/user/deleteuser.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')

        if username is None or email is None:
            context = {'info': '╭∩╮  输入不能为空  ╭∩╮'}
        elif not User.objects.filter(username=username, email=email):
            context = {'info': '╭∩╮  用户名/邮箱不匹配  ╭∩╮'}
        else:
            User.objects.get(username=username).delete()
            context = {'info': '丫  删除成功  丫'}
        return render(request, 'account/user/deleteuser.html', context)


@permission_required('account.user_manage')
@login_required
def adduser(request):
    if request.method == "GET":
        return render(request, 'account/user/adduser.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if username is None or email is None or last_name is None or first_name is None or password is None or password_confirm is None:
            context = {'info': '╭∩╮  输入不能为空  ╭∩╮'}
        elif password != password_confirm:
            context = {'info': '╭∩╮  两次密码不同  ╭∩╮'}
        elif User.objects.filter(username=username):
            context = {'info': '╭∩╮  用户名已经被注册  ╭∩╮'}
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            context = {'info': '丫  添加成功  丫'}
        return render(request, 'account/user/adduser.html', context)


@permission_required('account.user_manage')
@login_required
def modify_pw(request):
    if request.method == "GET":
        return render(request, 'account/user/modify_pw.html')
    else:
        uid = request.POST.get('uid')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password_confirm = request.POST.get('new_password_confirm')
        user = User.objects.get(id=uid)

        if old_password is None or new_password is None or new_password_confirm is None:
            context = {'info': '╭∩╮  输入不能为空  ╭∩╮'}
            return render(request, 'account/user/modify_pw.html', context)
        elif new_password != new_password_confirm:
            context = {'info': '╭∩╮  两次密码不同  ╭∩╮'}
            return render(request, 'account/user/modify_pw.html', context)
        elif check_password(old_password, user.password) is False:
            context = {'info': '╭∩╮  原密码错误  ╭∩╮'}
            return render(request, 'account/user/modify_pw.html', context)
        else:
            user.set_password(new_password)
            user.save()
            return HttpResponseRedirect(reverse('account:logout'))


@login_required
def modify_info(request):
    if request.method == "GET":
        return render(request, 'account/user/modify_info.html')
    else:
        uid = request.POST.get('uid')
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        user = User.objects.get(id=uid)
        if email is None or last_name is None or first_name is None:
            context = {'info': '╭∩╮  输入不能为空  ╭∩╮'}
            return render(request, 'account/user/modify_info.html', context)
        else:
            user.email = email
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            context = {'info': '丫  信息修改成功  丫'}
            return render(request, 'account/user/modify_info.html', context)