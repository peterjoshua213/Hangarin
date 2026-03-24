from django.contrib import admin
from .models import Priority, Category, Task, SubTask, Note

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['user']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['user']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'deadline', 'priority', 'category']
    list_filter = ['user', 'status', 'priority', 'category']
    search_fields = ['title', 'description']
    date_hierarchy = 'deadline'

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent_task_name']
    list_filter = ['status']
    search_fields = ['title']
    
    def parent_task_name(self, obj):
        return obj.task.title
    parent_task_name.short_description = 'Parent Task'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['task', 'content_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content']
    date_hierarchy = 'created_at'
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'