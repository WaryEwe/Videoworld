from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os, subprocess, ffmpeg
from django.conf import settings
import os, ffmpeg, subprocess
from hitcount.models import HitCountMixin
def gen_folder(instance, filename):
    user = instance.video_uploader.username
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(user, instance.id, file_extension)
    return "VideosUploaded/%s/%s" %(user, new_filename)

class VideoModel(models.Model, HitCountMixin):
    video_uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=40, null=False)
    video_description = models.TextField(max_length=70, null=True, blank=True)
    video_date = models.DateField(null=False, auto_now_add=True)
    video_src = models.FileField(upload_to=gen_folder, validators=[FileExtensionValidator(['mp4'])], null=False)
    video_thumb = models.ImageField(upload_to=gen_folder, null=True, blank=True)            
    video_view = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')


    def gen_thumb(self):
        video_path = self.video_src.path
        thumb_filename = f'{self.id}thumb.jpg'
        thumb_dir = os.path.join(settings.MEDIA_ROOT, 'thumbnail') 
        os.makedirs(thumb_dir, exist_ok=True)
        thumb_path = os.path.join(thumb_dir, thumb_filename)
        subprocess.call(['ffmpeg', '-i', video_path, '-ss', '00:00:00.000','-vframes', '1', '-f', 'image2', thumb_path])
        self.video_thumb = os.path.relpath(thumb_path, settings.MEDIA_ROOT)
        self.save_thumb(thumb_path)


    def save_thumb(self, thumb_path):
        super().save()

def __str__(self, video_id):
    return f'Video {self.video_id}'

