from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('upload/', views.upload_vid_view, name='upload_vid'),
    path('video/<int:video_id>/', views.video_view, name='video'),


]
