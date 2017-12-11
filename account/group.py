from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout #用户认证
from django.contrib.auth.models import User, Group, Permission

@permission_required('account.group_manage')
@login_required
def addgroup(request):
    if request.method == "GET":
        return render(request, 'account/group/addgroup.html')
    else:
        name = request.POST.get('name')

        if name is None:
            context = {'info': '╭∩╮  输入不能为空  ╭∩╮'}
        elif Group.objects.filter(name=name):
            context = {'info': '╭∩╮  用户组已存在  ╭∩╮'}
        else:
            Group.objects.create(name=name)
            context = {'info': '丫  添加成功  丫'}
        return render(request, 'account/group/addgroup.html', context)


@permission_required('account.group_manage')
@login_required
def deletegroup(request):
    context = {'users': User.objects.all(), 'groups': Group.objects.all()}
    if request.method == "GET":
        return render(request, 'account/group/deletegroup.html', context)
    else:
        name = request.POST.get('name')

        if name is None:
            context['info'] = '╭∩╮  输入不能为空  ╭∩╮'
        elif not Group.objects.filter(name=name):
            context['info'] = '╭∩╮  用户组不存在  ╭∩╮'
        else:
            Group.objects.get(name=name).delete()
            context['info'] = '丫  添加成功  丫'
        return render(request, 'account/group/deletegroup.html', context)

@permission_required('account.group_manage')
@login_required
def intogroup(request):
    context = {'users': User.objects.all(), 'groups': Group.objects.all()}
    if request.method == "GET":
        return render(request, 'account/group/intogroup.html', context)
    else:
        groupname = request.POST.get('groupname')
        username = request.POST.get('username')
        if groupname is None or username is None:
            context['info'] = '╭∩╮  输入不能为空  ╭∩╮'
        elif not Group.objects.filter(name=groupname):
            context['info'] = '╭∩╮  用户组不存在  ╭∩╮'
        elif not User.objects.filter(username=username):
            context['info'] = '╭∩╮  用户不存在  ╭∩╮'
        else:
            user = User.objects.get(username=username)
            group = Group.objects.get(name=groupname)
            group.user_set.add(user)
            context['info'] = '丫  添加成功  丫'
        return render(request, 'account/group/intogroup.html', context)


@permission_required('account.group_manage')
@login_required
def removegroup(request):
    context = {'users': User.objects.all(), 'groups': Group.objects.all()}
    if request.method == "GET":
        return render(request, 'account/group/removegroup.html', context)
    else:
        groupname = request.POST.get('groupname')
        username = request.POST.get('username')

        if groupname is None or username is None:
            context['info'] = '╭∩╮  输入不能为空  ╭∩╮'
        elif not Group.objects.filter(name=groupname):
            context['info'] = '╭∩╮  用户组不存在  ╭∩╮'
        elif not User.objects.filter(username=username):
            context['info'] = '╭∩╮  用户不存在  ╭∩╮'
        else:
            user = User.objects.get(username=username)
            group = Group.objects.get(name=groupname)
            group.user_set.remove(user)
            context['info'] = '丫  移除成功  丫'
        return render(request, 'account/group/removegroup.html', context)


@permission_required('account.group_manage')
@login_required
def addperm(request):
    context = {'groups': Group.objects.all(), 'perms': Permission.objects.all()}
    if request.method == "GET":
        return render(request, 'account/group/addperm.html', context)
    else:
        groupname = request.POST.get('groupname')
        permname = request.POST.get('permname')
        if groupname is None or permname is None:
            context['info'] = '╭∩╮  输入不能为空  ╭∩╮'
        elif not Group.objects.filter(name=groupname):
            context['info'] = '╭∩╮  用户组不存在  ╭∩╮'
        elif not Permission.objects.filter(name=permname):
            context['info'] = '╭∩╮  权限不存在  ╭∩╮'
        else:
            group = Group.objects.get(name=groupname)
            permission = Permission.objects.get(name=permname)
            group.permissions.add(permission)
            context['info'] = '丫  权限添加成功  丫'
        return render(request, 'account/group/addperm.html', context)


@permission_required('account.group_manage')
@login_required
def deleteperm(request):
    context = {'groups': Group.objects.all(), 'perms': Permission.objects.all()}
    if request.method == "GET":
        return render(request, 'account/group/deleteperm.html', context)
    else:
        groupname = request.POST.get('groupname')
        permname = request.POST.get('permname')

        if groupname is None or permname is None:
            context['info'] = '╭∩╮  输入不能为空  ╭∩╮'
        elif not Group.objects.filter(name=groupname):
            context['info'] = '╭∩╮  用户组不存在  ╭∩╮'
        elif not Permission.objects.filter(name=permname):
            context['info'] = '╭∩╮  权限不存在  ╭∩╮'
        else:
            group = Group.objects.get(name=groupname)
            permission = Permission.objects.get(name=permname)
            group.permissions.remove(permission)
            context['info'] = '丫  权限删除成功  丫'
        return render(request, 'account/group/deleteperm.html', context)