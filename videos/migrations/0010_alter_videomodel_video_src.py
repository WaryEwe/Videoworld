# Generated by Django 5.1.3 on 2024-12-12 14:55

import django.core.validators
import videos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_videomodel_video_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='video_src',
            field=models.FileField(upload_to=videos.models.gen_folder, validators=[django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
    ]
