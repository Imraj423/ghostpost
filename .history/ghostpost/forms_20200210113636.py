from django import forms


class addPost(forms.Form):
    title = forms.CharField(max_length=30)
    isRoast = forms.BooleanField()
    submitDate = forms.DateField()
    message = forms.CharField(widget='TextField')
    upvote = forms.IntegerField()
    downvote = forms.IntegerField()
