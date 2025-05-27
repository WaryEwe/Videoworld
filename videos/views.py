from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import VideoModel, CommentModel, CommentReplyModel
from .forms import VideoForm, CommentForm, CommentReplyForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView 
from hitcount.views import HitCountMixin
import users
from users import models

def home_view(request):
    username = models.ProfileModel.objects.filter()
    videos = VideoModel.objects.order_by('-video_date')
    accounts = models.ProfileModel.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    context = {
        'username':username,
        'videos':videos,
        'accounts':accounts,
    }
    return render(request, 'home.html', context)
@login_required(login_url='login')
def upload_vid_view(request):
    username = request.user.username
    url_user = reverse('user', kwargs={'username':username})
    video_thumb = VideoModel.objects.filter(video_uploader=request.user.id)
    if request.method == 'POST':
        video_f = VideoForm(request.POST, request.FILES)
        if video_f.is_valid():
            video_f_s = video_f.save(commit=False)
            video_f_s.video_uploader = request.user
            video_f_s.save()
            video_f_s.gen_thumb()
            return redirect('user', username=username)
    else:
        video_f = VideoForm()
    context = {
        'video_f':video_f,
        'username':username,
        'url_user':url_user,
    }
    return render(request, 'upload_vid.html', context)

def video_view(request, video_id):
    req_video = get_object_or_404(VideoModel, id=video_id)
    video_link = request.path.split('/')[-2] 
    video = VideoModel.objects.get(id=video_id)
    recommended_videos = VideoModel.objects.all()
    comments = CommentModel.objects.filter(comment_video=video_id)
    video_view = HitCount.objects.get_for_object(video)
    video_count = HitCountMixin.hit_count(request, video_view)
    video_likes = []
    if request.method == 'POST':
        comment_f = CommentForm(request.POST)
        if comment_f.is_valid():
            comment_f_s = comment_f.save(commit=False)
            comment_f_s.comment_author = request.user 
            comment_f_s.comment_video = req_video 
            comment_f_s.save()
            return redirect('video', video_id=video_link)
    else:
        comment_f = CommentForm()
    context = {
        'video_link':video_link,
        'video':video,
        'video_view':video_view,
        'comment_f':comment_f,
        'comments':comments,
        'recommended_videos':recommended_videos,
    }

    return render(request, 'video.html', context)

def search_view(request):
    query = request.GET.get('search_results')
    results = VideoModel.objects.filter(Q(video_title=query, video_desc=query))
    context = {
        'results':results,
        'query':query,
    }
    return render(request, 'search.html', context)
