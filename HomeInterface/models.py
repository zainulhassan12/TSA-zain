from django.contrib.auth.models import User
from django.db import models


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, auto_created=True, null=True)
    location = models.CharField(max_length=30, blank=False, null=False, verbose_name="Current Location")
    Age = models.IntegerField(max_length=None, verbose_name="Age")

    def __str__(self):
        return self.user.username
