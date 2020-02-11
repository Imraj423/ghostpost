from django import forms


class addPost(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    isRoast = forms.BooleanField()
    message = forms.CharField(widget=forms.TextInput)
    upvote = forms.IntegerField()
    downvote = forms.IntegerField()
