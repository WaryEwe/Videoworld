from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os, subprocess, ffmpeg

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
    def gen_thumbnail(instance, self):
        video_path = instance.video_src
        video_thumb_path = 'media/test' 
        subprocess.call(['ffmpeg', '-i', video_path, '-ss', '00:00:00.000','-vframes', '1', video_thumb_path])
def __str__(self, video_id):
    return f'Video {self.video_id}'
