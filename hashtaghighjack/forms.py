from django import forms


class DataForm(forms.Form):
    date = forms.DateField(help_text="Enter a date")