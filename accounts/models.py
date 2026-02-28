from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=150)
    degree = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
