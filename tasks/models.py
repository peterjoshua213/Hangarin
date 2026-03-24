from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='priorities')
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"
        unique_together = ['user', 'name']
    
    def __str__(self):
        return self.name

class Category(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        unique_together = ['user', 'name']
    
    def __str__(self):
        return self.name

class Task(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class SubTask(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Note(BaseModel):
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notes')
    
    def __str__(self):
        return f"Note for {self.task.title} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ['-created_at']