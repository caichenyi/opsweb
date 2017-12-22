from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from . import forms, models, sqlcheck


class CreateDBView(View):

    def get(self, request, *args, **kwargs):
        context = {'form': forms.CreateDBForm()}
        return render(request, 'sqldeploy/createdb.html', context=context)

    def post(self, request, *args, **kwargs):
        form = forms.CreateDBForm(request.POST)
        if form.is_valid():
            db_env = form.cleaned_data['db_env']
            db_name = form.cleaned_data['db_name']
            db_host = form.cleaned_data['db_host']
            db_port = form.cleaned_data['db_port']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if sqlcheck.mysql_connect(db_host=db_host, username=username, password=password, db_port=db_port, db_name=db_name):
                dbenv = models.DbEnv(db_env=form.cleaned_data['db_env'], db_name=form.cleaned_data['db_name'], db_host=form.cleaned_data['db_host'],
                                     db_port=form.cleaned_data['db_port'], username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                dbenv.save()
                context = {'form': form, 'info': '添加成功'}
            else:
                context = {'form': form, 'info': '数据库连接失败'}
        else:
            context = {'form': form, 'info': '两次密码不一致'}
        return render(request, 'sqldeploy/createdb.html', context=context)