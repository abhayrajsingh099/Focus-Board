"""
Urls for Tasks App
"""

from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('list_all/', views.ListAllTasksView, name='list_task'),
    path('detail/<int:id>/', views.TaskDetail, name='detail'),
    path('create/', views.CreateTask, name='create'),
    path('edit/<int:id>', views.EditTask, name='edit'),
    path('delete/<int:id>', views.DeleteTask, name='delete'),
]