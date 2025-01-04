from django import forms
from .models import VideoModel, CommentModel, CommentReplyModel

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['video_title', 'video_desc', 'video_src']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text']
class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReplyModel
        fields = ['reply_comment_text']

