# Generated by Django 5.1.3 on 2025-06-11 21:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_profilefollow_delete_followers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profilefollow',
            unique_together={('follower', 'following')},
        ),
    ]
