# Generated by Django 4.0.2 on 2022-05-29 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_liked_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='liked_posts',
            new_name='read_posts',
        ),
    ]
