from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=False, null=True, unique=True)
    email = models.EmailField(unique=True)
    genres = models.CharField(max_length=500)
    services = models.CharField(max_length=500)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # add related name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',  # add related name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username
