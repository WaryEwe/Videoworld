from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignupForm, ProfileForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import ProfileModel
from django.urls import reverse
from videos import models
def login_view(request):
    if request.method == 'POST':
        login_f = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user', username=username)
        else:
            pass
    else:
        login_f = LoginForm()
    context = {
        'login_f': login_f,
    }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        signup_f = SignupForm(request.POST)
        if signup_f.is_valid():
            signup_f.save()
            return redirect('login')
    else:
        signup_f = SignupForm()
    context = {
        'signup_f': signup_f,
    }
    return render(request, 'signup.html', context)

def profile_view(request, username):
   req_user = get_object_or_404(User, username=username)
   curr_user, created = ProfileModel.objects.get_or_create(user_id=req_user) 
   videos = models.VideoModel.objects.filter(video_uploader=req_user) 
   url_user = reverse('user', kwargs={'username': username})
   if request.method == 'POST':
        user_f = ProfileForm(request.POST, request.FILES, instance=req_user)
        if user_f.is_valid():
            user_f.save()
            return redirect('user', username=username)

   else:
        user_f = ProfileForm(instance=req_user)

   context = {
        'username': username,
        'req_user': req_user,
        'videos': videos,
        'user_f':user_f,
        'curr_user':curr_user,
    }
   return render(request, 'profile.html', context)


