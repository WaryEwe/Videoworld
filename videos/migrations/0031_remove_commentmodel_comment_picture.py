# Generated by Django 5.1.3 on 2024-12-30 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0030_alter_commentmodel_comment_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='comment_picture',
        ),
    ]
