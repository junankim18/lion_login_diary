from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    nickname = models.CharField(verbose_name='닉네임', max_length=100)
