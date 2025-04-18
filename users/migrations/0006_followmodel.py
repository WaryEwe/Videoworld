# Generated by Django 5.1.3 on 2025-01-01 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profilemodel_user_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_date', models.DateField(auto_now_add=True)),
                ('user_follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to='users.profilemodel')),
                ('user_you', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curr_user', to='users.profilemodel')),
            ],
        ),
    ]
