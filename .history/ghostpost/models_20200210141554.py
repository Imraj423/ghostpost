from django.utils import timezone
from django.db import models


class ghostPost(models.Model):
    message = models.CharField(max_length=280)
    isRoast = models.BooleanField()
    submitDate = models.DateField(auto_now=False, auto_now_add=True)
    total = models.IntegerField(default=0)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.message
