from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.username