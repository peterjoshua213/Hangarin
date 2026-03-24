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
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User "{username}" does not exist'))
            return
        
        # Get user's priorities and categories
        priorities = list(Priority.objects.filter(user=user))
        categories = list(Category.objects.filter(user=user))
        
        if not priorities:
            self.stdout.write(self.style.ERROR('No priorities found for this user'))
            return
        
        if not categories:
            self.stdout.write(self.style.ERROR('No categories found for this user'))
            return
        
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
