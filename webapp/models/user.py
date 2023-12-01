from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add additional fields if needed
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self)-> str:
        return self.username
