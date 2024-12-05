from django.db import models
from django.contrib.auth.models import User

class VideoModel(models.Model):
    video_uploader = models.ForeinKey(User, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=70, null=False)
    video_src = models.FileField(upload_to='videos_uploaded', null=False)
    video_date = models.DateField()
