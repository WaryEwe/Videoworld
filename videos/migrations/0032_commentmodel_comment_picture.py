# Generated by Django 5.1.3 on 2025-01-04 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_followmodel'),
        ('videos', '0031_remove_commentmodel_comment_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='comment_picture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profilemodel'),
        ),
    ]
