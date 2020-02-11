from django import forms


class addPost(forms.Form):
    message = forms.CharField(widget=forms.TextInput, max_length=280)
    is_Boast = forms.BooleanField(
        widget=forms.CheckboxSelectMultiple(None, choices=((True, 'Boast'),(False, 'Roast')))
