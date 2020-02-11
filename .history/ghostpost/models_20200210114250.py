from django.db import models
from forms.addPost import title


class ghostPost(models.Model):
    title = models.CharField(max_length=30)
    isRoast = models.BooleanField()
    submitDate = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
