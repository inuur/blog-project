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
        blank=True
    )

    def __str__(self):
        return f"{self.author.username}'s blog"


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=140, blank=True, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    def __str__(self):
        return self.title
