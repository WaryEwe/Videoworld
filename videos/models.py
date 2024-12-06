from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import uuid

class VideoModel(models.Model):
    video_uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=40, null=False)
    video_description = models.TextField(max_length=70, null=True, blank=True)
    video_src = models.FileField(upload_to='videos_uploaded', validators=[FileExtensionValidator(['mp4'])], null=False)
    video_date = models.DateField(null=False, auto_now_add=True)

def __str__(self, video_id):
    return f'Video {self.video_id}'
