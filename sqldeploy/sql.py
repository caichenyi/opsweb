from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone

from . import forms, models, sqlcheck


class SubmitSqlView(View):

    def get(self, request, *args, **kwargs):
        context = {'form': forms.SubmitSqlForm()}
        return render(request, 'sqldeploy/submitsql.html', context=context)

    def post(self, request, *args, **kwargs):
        form = forms.SubmitSqlForm(request.POST)
        if form.is_valid():
            sqlinfo = models.SqlInfo(title=form.cleaned_data['title'], content=form.cleaned_data['content'], status=0, submiter=request.user.id, db_env=form.cleaned_data['db_env'].id, submit_time=timezone.now())
            sqlinfo.save()
            context = {'form': form, 'info': '提交成功'}
            return render(request, 'sqldeploy/submitsql.html', context=context)
        else:
            context = {'form': form, 'info': '自检失败'}
            return render(request, 'sqldeploy/submitsql.html', context=context)


class SqlListView(View):

    def get(self, request, *args, **kwargs):
        context = kwargs
        if kwargs['status'] == '5':
            sqllist = models.SqlInfo.objects.all()
        else:
            sqllist = models.SqlInfo.objects.filter(status=kwargs['status'])
        context['sqllist'] = sqllist
        return render(request, 'sqldeploy/sqllist.html', context=context)


class SqlDropView(View):

    def get(self, request, *args, **kwargs):
        sqlinfo = models.SqlInfo.objects.get(id=kwargs['id'])
        sqlinfo.status = 4
        sqlinfo.dropper = kwargs['user_id']
        sqlinfo.save()
        return HttpResponseRedirect(reverse('sqldeploy:sqllist', args=(5,)))


class SqlReviewView(View):

    def get(self, request, *args, **kwargs):
        sqlinfo = models.SqlInfo.objects.get(id=kwargs['id'])
        if sqlinfo.status == 0:
            sqlinfo.dev_reviewer = kwargs['user_id']
        elif sqlinfo.status == 1:
            sqlinfo.dba_reviewer = kwargs['user_id']
        elif sqlinfo.status == 2:
            sqlinfo.intergrator = kwargs['user_id']
            dbenv = models.DbEnv.objects.get(id=sqlinfo.db_env)
            sqlcheck.sql_deploy(dbenv=dbenv, content=sqlinfo.content)
            sqlinfo.intergrate_time = timezone.now()
        sqlinfo.status = sqlinfo.status + 1
        sqlinfo.save()
        return HttpResponseRedirect(reverse('sqldeploy:sqllist', args=(5,)))

