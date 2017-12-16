from django.shortcuts import render
from django.utils import timezone

from . import forms, models
# Create your views here.

def submit(request):
    if request.method == "GET":
        context = {'form': forms.SubmitForm()}
        return render(request, 'sqldeploy/submit.html', context=context)
    else:
        form = forms.SubmitForm(request.POST)
        if form.is_valid():
            sql = models.SqlInfo(title=form.cleaned_data['title'], submiter=request.user.id, content=form.cleaned_data['content'], status=0, submit_time=timezone.now())
            print(sql)
            sql.save()
            return render(request, 'index.html')