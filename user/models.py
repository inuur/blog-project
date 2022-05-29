from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    read_posts = models.ManyToManyField(
        'api.Post',
        blank=True
    )
