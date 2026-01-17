from django.urls import path

from . import api_views

urlpatterns = [
    path('list_all/', api_views.task_list, name='list_all'),
    path('detail/<int:id>', api_views.task_detail, name='detail_task'),
    path('create/', api_views.create_task, name='create_task'),
    path('update/<int:id>', api_views.update_task, name='update_task'),
    path('update-patch/<int:id>', api_views.update_patch, name='update_patch'),
    path('delete/<int:id>', api_views.delete_task, name='delete_task'),
]
