from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
def home_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    context = {
        'username':username,
    }

    return render(request, 'home.html', context)
