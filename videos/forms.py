from django import forms
from .models import VideoModel, CommentModel, CommentReplyModel

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['video_title', 'video_desc', 'video_src']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['video_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['video_desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['video_src'].widget.attrs.update({'class': 'form-control'})



class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text']
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['comment_text'].widget.attrs.update({'class': 'form-control'})

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReplyModel
        fields = ['reply_comment_text']

class SearchForm(forms.ModelForm):
    query = forms.CharField(label="Search")
