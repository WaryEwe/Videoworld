from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignupForm, ProfileForm, ProfileSettingsForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import ProfileModel
from django.urls import reverse
from videos import models
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView 
from hitcount.views import HitCountMixin
from django.contrib.auth.decorators import login_required

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
   videos = models.VideoModel.objects.filter(video_uploader=req_user).order_by('-video_date')
   url_user = reverse('user', kwargs={'username': username})
   img_user = ProfileModel.objects.filter(user_id=req_user.id)
   if request.method == 'POST':
        user_f = ProfileForm(request.POST, request.FILES, instance=curr_user) 
        if user_f.is_valid(): 
            user_f.save()
            return redirect('user', username=username)
   else: 
        user_f = ProfileForm(instance=curr_user) 
   context = {
        'username': username,
        'req_user': req_user,
        'videos': videos,
        'user_f':user_f,
        'curr_user':curr_user,
        'img_user':img_user,

    }
   return render(request, 'profile.html', context)
def id_profile_view(request, user_id):
    req_user = get_object_or_404(User, id=user_id)
    return redirect('user', username=req_user)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')

@login_required(login_url='login')
def settings_view(request):
    if request.method == 'POST':
        change_username = ProfileSettingsForm(request.POST, instance=request.user)
        if change_username.is_valid():
            change_username.save()
            return redirect('settings')

    else:
        change_username = ProfileSettingsForm(instance=request.user)
    context = {
        'change_username':change_username
    }
    return render(request, 'settings.html', context)

@login_required(login_url='login')
def delete_view(request, username):
    request.user.delete()
    return redirect('home')

    
