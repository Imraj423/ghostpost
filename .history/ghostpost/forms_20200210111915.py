from django import forms



class mainform(forms.Form):
    title = forms.CharField(max_length=30)
    isRoast = forms.BooleanField()
    submitDate = forms.DateField(auto_now=False, auto_now_add=True)
    message = forms.TextField()
    upvote = forms.IntegerField()
    downvote = forms.IntegerField()

