from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ProfileModel 
class LoginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['user_desc', 'user_banner', 'user_picture']
