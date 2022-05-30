from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Generates a lot of data based on models and saves it into the database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass
