from django.utils import timezone
from django.db import models


class ghostPost(models.Model):
    message = models.CharField(max_length=280)
    isRoast = models.BooleanField()
    submitDate = models.DateField(auto_now=False, auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Post(models.Model):
    body = models.CharField(max_length=280)
    is_boast = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
