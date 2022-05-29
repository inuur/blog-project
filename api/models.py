from django.db import models
from user.models import User


class Blog(models.Model):
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='author'
    )
    followers = models.ManyToManyField(
        User,
        related_name='followed_blogs',
    )

    def __str__(self):
        return f"{self.author.username}'s blog"
