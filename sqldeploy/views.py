from django.shortcuts import render

from . import forms
# Create your views here.

def submit(request):
    if request.method == "GET":
        form = forms.SubmitForm()
        context = {'form': form}
        return render(request, 'sqldeploy/submit.html', context=context)
    else:
        return render(request, 'index.html')