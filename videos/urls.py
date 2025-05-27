from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('upload/', views.upload_vid_view, name='upload'),
    path('video/<int:video_id>/', views.video_view, name='video'),
    path('search/', views.search_view, name='search'),
]
