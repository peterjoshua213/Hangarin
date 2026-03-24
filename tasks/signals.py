from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Priority, Category

DEFAULT_PRIORITIES = ['High', 'Medium', 'Low']
DEFAULT_CATEGORIES = ['Work', 'Personal', 'Shopping', 'Health', 'Other']


@receiver(post_save, sender=User)
def create_default_priorities_and_categories(sender, instance, created, **kwargs):
    """
    Create default priorities and categories when a new user is created.
    """
    if created:
        # Create default priorities
        for priority_name in DEFAULT_PRIORITIES:
            Priority.objects.get_or_create(
                user=instance,
                name=priority_name
            )
        
        # Create default categories
        for category_name in DEFAULT_CATEGORIES:
            Category.objects.get_or_create(
                user=instance,
                name=category_name
            )
