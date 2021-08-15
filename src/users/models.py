from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=50, unique=True, editable=False, db_index=True)
    last_request = models.DateTimeField(verbose_name='last made request', blank=True, null=True)
    objects = UserManager()

    def __str__(self):
        return self.username
