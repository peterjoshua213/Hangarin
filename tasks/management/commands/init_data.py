from django.core.management.base import BaseCommand
from tasks.models import Priority, Category


class Command(BaseCommand):
    help = 'Initialize default priorities and categories for tasks'

    def handle(self, *args, **options):
        # Default priorities
        priorities_data = [
            {'name': 'High'},
            {'name': 'Medium'},
            {'name': 'Low'},
        ]

        # Default categories
        categories_data = [
            {'name': 'Work'},
            {'name': 'Personal'},
            {'name': 'Shopping'},
            {'name': 'Health'},
            {'name': 'Learning'},
            {'name': 'Projects'},
            {'name': 'Home'},
            {'name': 'Finance'},
        ]

        # Create priorities
        created_priorities = 0
        for priority_data in priorities_data:
            priority, created = Priority.objects.get_or_create(**priority_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created priority: {priority.name}')
                )
                created_priorities += 1

        if created_priorities == 0:
            self.stdout.write('• All priorities already exist')

        # Create categories
        created_categories = 0
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created category: {category.name}')
                )
                created_categories += 1

        if created_categories == 0:
            self.stdout.write('• All categories already exist')

        # Summary
        total_priorities = Priority.objects.count()
        total_categories = Category.objects.count()
        
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✅ Initialization Complete!'))
        self.stdout.write(f'📊 Total Priorities: {total_priorities}')
        self.stdout.write(f'📁 Total Categories: {total_categories}')
