from django import forms


class addPost(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    isRoast = forms.BooleanField()
    submitDate = forms.DateField()
    message = forms.CharField(widget=forms.TextInput)
    upvote = forms.IntegerField(default=0)
    downvote = forms.IntegerField(default=0)
