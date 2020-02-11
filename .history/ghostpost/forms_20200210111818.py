from django import forms
from crispy_forms.helper import FormHelper
from ghostpost.models import ghostPost


class mainform(forms.Form):
    title = models.CharField(max_length=30)
    isRoast = models.BooleanField()
    submitDate = models.DateField(auto_now=False, auto_now_add=True)
    message = models.TextField()
    upvote = models.IntegerField()
    downvote = models.IntegerField()

