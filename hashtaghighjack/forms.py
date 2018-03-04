from django import forms
from hashtaghighjack.models import Data


class DataForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(),
        label='Enter Date'
    )
    tag = forms.CharField(
        widget=forms.TextInput(),
        max_length=15,
        label='Enter # tag'
    )

    class Meta:
        model = Data
        fields = ('date', 'tag')
