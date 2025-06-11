from django.db import models
from django.contrib.auth.models import User
import os

class ProfileModel(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_desc = models.CharField(max_length=40, null=True, blank=True)
    user_banner = models.ImageField(default='default/banner-5185316.jpg', upload_to='profile_images/')
    user_picture = models.ImageField(default='default/Default_pfp.jpg', upload_to='profile_images')
    def __str__(self, user_id, user_banner):
        return self.user_id.user_banner

class ProfileFollow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['follower', 'following']
