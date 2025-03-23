from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_membership = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=True)
    ROLE_CHOICES = (("admin", "Admin"), ("user", "User"))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")

    def __str__(self):
        return self.username