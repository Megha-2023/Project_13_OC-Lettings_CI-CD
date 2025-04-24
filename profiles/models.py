""" Module contains Profile model"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """ Model class for Profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
