from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomAccount(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
