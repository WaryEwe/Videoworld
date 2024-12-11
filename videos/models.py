from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os,ffpmeg
class VideoModel(models.Model):
    video_uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=40, null=False)
    video_description = models.TextField(max_length=70, null=True, blank=True)
    video_date = models.DateField(null=False, auto_now_add=True)
    video_src = models.FileField(upload_to='videos_uploaded', validators=[FileExtensionValidator(['mp4'])], null=False)
    video_thumb = models.ImageField(upload_to='videos_uploaded/video_thumbnails', null=True, blank=True)
    def gen_thumbnail(video_path, output_name, time="00:03"):
        thumbnail_path = os.path.join(settings.MEDIA_ROOT, 'thumbnails', output_name)
        ffmpeg.input(video_path, ss=time).output(thumbnail_path, vframes=1, qscale:v=2).run()
def __str__(self, video_id):
    return f'Video {self.video_id}'
