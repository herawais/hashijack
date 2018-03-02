from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def hijack(request):
    form = forms.DataForm()
    if request.method == 'post':
        form = forms.DataForm(request.post)
        print("Date is entered")

        if form.is_valid():
            print("Date is valid entered")

        print(form.cleaned_data['date'])
    return render(request, 'hashtaghijack/hijack.html', {'dataform':form})


