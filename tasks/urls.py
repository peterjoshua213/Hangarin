"""
URL configuration for tasks app.
"""
from django.urls import path
from . import views
from . import views_manage

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
    
    # SubTask URLs
    path('tasks/<int:task_id>/subtasks/create/', views.create_subtask, name='create-subtask'),
    path('tasks/<int:task_id>/subtasks/<int:subtask_id>/edit/', views.update_subtask, name='update-subtask'),
    path('tasks/<int:task_id>/subtasks/<int:subtask_id>/delete/', views.delete_subtask, name='delete-subtask'),
    
    # Note URLs
    path('tasks/<int:task_id>/notes/create/', views.create_note, name='create-note'),
    path('tasks/<int:task_id>/notes/<int:note_id>/edit/', views.update_note, name='update-note'),
    path('tasks/<int:task_id>/notes/<int:note_id>/delete/', views.delete_note, name='delete-note'),
    
    # Priority Management URLs
    path('priorities/', views_manage.priority_list, name='priority-list'),
    path('priorities/create/', views_manage.create_priority, name='create-priority'),
    path('priorities/<int:priority_id>/edit/', views_manage.update_priority, name='update-priority'),
    path('priorities/<int:priority_id>/delete/', views_manage.delete_priority, name='delete-priority'),
    
    # Category Management URLs
    path('categories/', views_manage.category_list, name='category-list'),
    path('categories/create/', views_manage.create_category, name='create-category'),
    path('categories/<int:category_id>/edit/', views_manage.update_category, name='update-category'),
    path('categories/<int:category_id>/delete/', views_manage.delete_category, name='delete-category'),
    
    # API Endpoints
    path('api/tasks/', views.task_list_api, name='api-task-list'),
    path('api/tasks/<int:task_id>/', views.task_detail_api, name='api-task-detail'),
]
