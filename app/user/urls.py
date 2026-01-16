"""
Url mapping for user authentication handling.
"""

from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    # path('register/', views.regsiterView, name='register'),
]