from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # pass
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True)
    genres = models.CharField(max_length=500)
    services = models.CharField(max_length=500)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'genres', 'services']

    def __str__(self):
        return "{}".format(self.email)
