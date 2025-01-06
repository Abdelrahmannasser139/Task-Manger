# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Task list page
    path('add/', views.add_task, name='add_task'),  # Add new task page
    path('edit/<int:id>/', views.edit_task, name='edit_task'),  # Edit task page
    path('delete/<int:id>/', views.delete_task, name='delete_task'),  # Delete task page
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),

]

