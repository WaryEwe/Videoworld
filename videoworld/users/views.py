from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignupForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import ProfileModel
from django.urls import reverse

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
   url_user = reverse('user', kwargs={'username': username})
   context = {
        'username': username,
        'req_user': req_user,
    }
   return render(request, 'profile.html', context)


