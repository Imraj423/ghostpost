from django import forms


class addPost(forms.Form):
    
    isRoast = forms.BooleanField()
    message = forms.CharField(widget=forms.TextInput, max_length=280)
