from django import forms


class addPost(forms.Form):
    message = forms.CharField(widget=forms.TextInput, max_length=280)
    submitDate = models.DateTimeField(auto_now=False, auto_now_add=True)
