from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def hijack(request):
    msg = "hello this is a message"
    form = forms.DataForm()
    if request.method == 'post':
        form = forms.DataForm(request.POST)
        print("Date is entered")

        if form.is_valid():
            print("Date is valid entered")
            msg = form.cleaned_data['date']
    return render(request, 'hashtaghijack/hijack.html', {'dataform':form, 'message':msg})


