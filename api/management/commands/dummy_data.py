import random

from django.core.management import BaseCommand
from mixer.backend.django import mixer


class Command(BaseCommand):
    help = 'Generates a lot of data based on models and saves it into the database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        superuser = mixer.blend('user.User', username='root', is_superuser=True)
        superuser.set_password('123')
        superuser.save()
        users = mixer.cycle(50000).blend('user.User')
        users.append(superuser)

        for user in users:
            blogs = list(map(lambda usr: usr.blog, random.choices(users, k=100)))
            user.followed_blogs.add(*blogs)

        for _ in range(200000):
            mixer.blend('api.post', blog=random.choice(users).blog)
