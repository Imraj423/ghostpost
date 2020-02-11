from django.db import models


class ghostPost(models.Model):
    title = models.CharField(max_length=30)
    isRoast = models.BooleanField()
    submitDate = models.DateField(auto_now=False, auto_now_add=True)
    message = models.CharField(max_length=30)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.title
