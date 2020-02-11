from django.db import models


def ghostPost(models.Model):
    title = models.CharField(max_length=30)
    isRoast = models.BooleanField(widget=CheckboxInput)
    submitDate = models.DateField(auto_now=False, auto_now_add=True)
    message = models.TextField()
