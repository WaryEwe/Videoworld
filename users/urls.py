from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('user/<str:username>/', views.profile_view, name='user'),
    path('<int:user_id>/', views.id_profile_view, name='id_user'),
]
