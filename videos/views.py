from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import VideoModel
from .forms import VideoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from users import models

def home_view(request): 
    videos = VideoModel.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    context = {
        'username':username,
        'videos':videos,
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
    video_link = get_object_or_404(VideoModel, id=video_id)
    video_link = request.path.split('/')[-2] 
    video = VideoModel.objects.get(id=video_id)
    username = models.ProfileModel.objects.filter()
    context = {
        'video_link':video_link,
        'video':video,
        'username':username,
    }
    return render(request, 'video.html', context)









