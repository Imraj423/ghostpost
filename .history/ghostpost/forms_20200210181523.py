from django import forms


class addPost(forms.Form):
    message = forms.CharField(widget=forms.TextInput, max_length=280)
    OPTIONS = (
        (True, "Boast"),
        (False, "Roast"))
    is_Boast = forms.BooleanField(
        widget=forms.CheckboxSelectMultiple(choices=OPTIONS))
