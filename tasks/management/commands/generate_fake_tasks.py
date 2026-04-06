from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from faker import Faker
from tasks.models import Task, Priority, Category
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake tasks for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of tasks to create (default: 10)'
        )
        parser.add_argument(
            '--username',
            type=str,
            default='testuser',
            help='Username to create tasks for (default: testuser)'
        )

    def handle(self, *args, **options):
        count = options['count']
        username = options['username']
        
        # Create user if doesn't exist
        try:
            user = User.objects.get(username=username)
            self.stdout.write(f'Using existing user: {username}')
        except User.DoesNotExist:
            self.stdout.write(f'Creating new user: {username}')
            user = User.objects.create_user(username=username, password='Password123!')
        
        # Create default priorities if they don't exist
        priorities = list(Priority.objects.filter(user=user))
        if not priorities:
            self.stdout.write('Creating default priorities...')
            default_priorities = ['High', 'Medium', 'Low']
            for priority_name in default_priorities:
                Priority.objects.get_or_create(user=user, name=priority_name)
            priorities = list(Priority.objects.filter(user=user))
        
        # Create default categories if they don't exist
        categories = list(Category.objects.filter(user=user))
        if not categories:
            self.stdout.write('Creating default categories...')
            default_categories = ['Work', 'Personal', 'Shopping', 'Health', 'Other']
            for category_name in default_categories:
                Category.objects.get_or_create(user=user, name=category_name)
            categories = list(Category.objects.filter(user=user))
        
        status_choices = ['Pending', 'In Progress', 'Completed']
        
        created_tasks = []
        
        for i in range(count):
            # Generate random data
            title = fake.sentence(nb_words=4)
            description = fake.paragraph(nb_sentences=3)
            status = random.choice(status_choices)
            priority = random.choice(priorities)
            category = random.choice(categories)
            
            # Random deadline between now and 30 days from now
            days_ahead = random.randint(1, 30)
            deadline = timezone.now() + timedelta(days=days_ahead)
            
            task = Task.objects.create(
                user=user,
                title=title,
                description=description,
                status=status,
                priority=priority,
                category=category,
                deadline=deadline
            )
            created_tasks.append(task)
            self.stdout.write(f'{i+1}. {task.title} (Status: {task.status})')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Successfully created {len(created_tasks)} fake tasks for {username}!'
            )
        )
