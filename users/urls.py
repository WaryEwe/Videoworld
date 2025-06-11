from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('user/<str:username>/', views.profile_view, name='user'),
    path('<int:user_id>/', views.id_profile_view, name='user_id_url'),
    path('logout', views.logout_view, name='logout'),
    path('settings/', views.settings_view, name='settings'),
    path('user/<str:username>/delete', views.delete_user, name='delete'),
    path('follow/<int:user_id>', views.follow_user, name='follow'),
    path('unfollow/<int:user_id>', views.unfollow_user, name='unfollow'),
]
