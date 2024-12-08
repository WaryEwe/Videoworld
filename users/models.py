from django.db import models
from django.contrib.auth.models import User
import os
class ProfileModel(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_desc = models.CharField(max_length=40, null=True, blank=True)
    user_banner = models.ImageField(default='', upload_to='profile_images/')
    def __str__(self, user_id):
        return self.user_id.username
