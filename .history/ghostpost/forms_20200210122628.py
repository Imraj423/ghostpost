from django import forms


class addPost(forms.Form):
    title = forms.CharField(max_length=30)
    isRoast = models.BooleanField()
    submitDate = models.DateField(auto_now=False, auto_now_add=True)
    message = models.CharField(widget=forms.Textarea)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
