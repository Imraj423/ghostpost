from django import forms


class addPost(forms.Form):
    message = forms.CharField(widget=forms.TextInput, max_length=280)
    submitDate = forms.DateField()
