# Generated by Django 5.1.3 on 2025-06-11 21:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_followers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
    ]
