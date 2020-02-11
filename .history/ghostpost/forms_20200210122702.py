from django import forms


class addPost(forms.Form):
    title = forms.CharField(max_lengtforms    
    isRoast = forms.BooleanField()
    submitDate = forms.DateField(auto_now=False, auto_now_add=True)
    message = forms.CharField(widget=forms.Textarea)
    upvote = forms.IntegerField(default=0)
    downvote = forms.IntegerField(default=0)
