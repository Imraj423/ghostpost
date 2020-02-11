from django.db import models
from django.utils import timezone


class ghostPost(models.Model):
    message = models.CharField(max_length=280)
    time = models.DateTimeField(default=timezone.now)
    is_Boast = models.BooleanField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    key = models.join(random.choice(string.ascii_uppercase) for _ in range(8))

    def __str__(self):
        return self.message
