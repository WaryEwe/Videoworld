from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os, ffmpeg, subprocess

def gen_folder(instance, filename):
    user = instance.video_uploader.username
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(user, instance.id, file_extension)
    return "MyFolder/%s/%s" %(user, new_filename)
class VideoModel(models.Model):
    video_uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=40, null=False)
    video_description = models.TextField(max_length=70, null=True, blank=True)
    video_date = models.DateField(null=False, auto_now_add=True)
    video_src = models.FileField(upload_to=gen_folder, validators=[FileExtensionValidator(['mp4'])], null=False)
    video_thumb = models.ImageField(upload_to=gen_folder, null=True, blank=True)
def __str__(self, video_id):
    return f'Video {self.video_id}'
