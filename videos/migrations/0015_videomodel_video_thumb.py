# Generated by Django 5.1.3 on 2024-12-16 09:48

import videos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_merge_20241216_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='video_thumb',
            field=models.ImageField(blank=True, null=True, upload_to=videos.models.gen_folder),
        ),
    ]
