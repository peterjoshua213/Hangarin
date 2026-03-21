"""
URL configuration for tasks app.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard-alt'),
    
    # Task List & Detail
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task-detail'),
    
    # Create Task
    path('tasks/create/', views.create_task, name='create-task'),
    
    # Update Task
    path('tasks/<int:task_id>/edit/', views.update_task, name='update-task'),
    
    # Delete Task
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete-task'),
    
    # API Endpoints
    path('api/tasks/', views.task_list_api, name='api-task-list'),
    path('api/tasks/<int:task_id>/', views.task_detail_api, name='api-task-detail'),
]
