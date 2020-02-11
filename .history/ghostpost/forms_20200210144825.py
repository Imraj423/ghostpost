from django import forms
from django.utils import timezone


class addPost(forms.Form):
    message = forms.CharField(widget=forms.TextInput, max_length=280)
    submitDate = forms.DateField(default=timezone.now)
