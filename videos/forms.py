from django import forms
from .models import VideoModel
class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['video_title', 'video_description', 'video_src',]

