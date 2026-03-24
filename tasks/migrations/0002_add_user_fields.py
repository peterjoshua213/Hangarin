# Generated migration to add user fields and make Priority/Category user-specific

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def delete_existing_data(apps, schema_editor):
    """Delete existing Priority, Category, and Task data to avoid conflicts"""
    Priority = apps.get_model('tasks', 'Priority')
    Category = apps.get_model('tasks', 'Category')
    Task = apps.get_model('tasks', 'Task')
    
    Task.objects.all().delete()
    Priority.objects.all().delete()
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        # Delete existing data to avoid conflicts with new constraints
        migrations.RunPython(delete_existing_data),
        
        # Add user field to Priority
        migrations.AddField(
            model_name='priority',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='priorities', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        
        # Remove old Priority unique constraint and replace with user-based constraint
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddConstraint(
            model_name='priority',
            constraint=models.UniqueConstraint(fields=['user', 'name'], name='unique_user_priority_name'),
        ),
        
        # Add user field to Category
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        
        # Remove old Category unique constraint and replace with user-based constraint
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=['user', 'name'], name='unique_user_category_name'),
        ),
        
        # Add user field to Task
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        
        # Update Task's foreign keys to be nullable
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='tasks.priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='tasks.category'),
        ),
    ]
