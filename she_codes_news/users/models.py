# from django.db import models

# # Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


# Define the "UserProfile" model:
class UserProfile(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.username