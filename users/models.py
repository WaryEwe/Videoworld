from django.db import models
from django.contrib.auth.models import User
import os
class ProfileModel(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_desc = models.CharField(max_length=40, null=True, blank=True)
    user_banner = models.ImageField(default='default/banner-5185316.jpg', upload_to='profile_images/')
    user_picture = models.ImageField(default='default/Default_pfp.jpg', upload_to='profile_images')
    user_followers = models.IntegerField(default=0, null=False)
    def __str__(self, user_id, user_banner):
        return self.user_id.user_banner

