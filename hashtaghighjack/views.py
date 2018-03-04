from django.shortcuts import render
from . import forms
from .models import Data


def hijack(request):
    title = "Date Picker"
    form = forms.DataForm()
    data = Data.objects.all()
    if request.method == 'POST':
        form = forms.DataForm(request.POST)
        print("Date is entered")
        if form.is_valid():
            form.save()

    return render(request, 'hashtaghijack/tabs.html', {'dataform': form, 'title': title, 'data': data})


