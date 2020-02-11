from django import forms


class addPost(forms.Form):
    title = forms.CharField(widget=forms.TextInput, max_length=30)
    isRoast = forms.BooleanField()
    message = forms.CharField(widget=forms.TextInput, max_length=280)
