from django.db import models
from django.utils import timezone


class ghostPost(models.Model):
    message = models.CharField(max_length=280)
    time = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    

    def __str__(self):
        return self.message
