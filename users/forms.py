from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ProfileModel 
from django.forms import FileInput

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_picture'].widget = FileInput()
        self.fields['user_picture'].widget.attrs.update({'class': 'form-control'})
        self.fields['user_banner'].widget = FileInput()
        self.fields['user_banner'].widget.attrs.update({'class': 'form-control'})


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
