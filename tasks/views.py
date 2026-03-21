from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Task, Priority, Category

# Task List View
@login_required
@require_http_methods(["GET"])
def task_list(request):
    """
    Display all tasks with optional filtering by status, priority, or category.
    GET parameters: status, priority_id, category_id
    """
    tasks = Task.objects.all()
    
    # Filter by status if provided
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)
    
    # Filter by priority if provided
    priority_id = request.GET.get('priority_id')
    if priority_id:
        tasks = tasks.filter(priority_id=priority_id)
    
    # Filter by category if provided
    category_id = request.GET.get('category_id')
    if category_id:
        tasks = tasks.filter(category_id=category_id)
    
    context = {
        'tasks': tasks,
        'priorities': Priority.objects.all().order_by('name'),
        'categories': Category.objects.all().order_by('name'),
    }
    return render(request, 'tasks/task_list.html', context)


# Task Detail View
@login_required
@require_http_methods(["GET"])
def task_detail(request, task_id):
    """
    Display details of a specific task.
    """
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)


# Create Task View
@login_required
@require_http_methods(["GET", "POST"])
def create_task(request):
    """
    Create a new task.
    GET: Display form
    POST: Save new task
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        status = request.POST.get('status', 'Pending')
        deadline = request.POST.get('deadline', None)
        priority_id = request.POST.get('priority_id')
        category_id = request.POST.get('category_id')
        
        # Validate required fields
        if not title:
            return render(request, 'tasks/create_task.html', {
                'error': 'Task title is required',
                'priorities': Priority.objects.all(),
                'categories': Category.objects.all(),
            })
        
        # Create the task
        task = Task.objects.create(
            title=title,
            description=description,
            status=status,
            deadline=deadline if deadline else None,
            priority_id=priority_id if priority_id else None,
            category_id=category_id if category_id else None,
        )
        
        return redirect('task-detail', task_id=task.id)
    
    context = {
        'priorities': Priority.objects.all().order_by('name'),
        'categories': Category.objects.all().order_by('name'),
    }
    return render(request, 'tasks/create_task.html', context)


# Update Task View
@login_required
@require_http_methods(["GET", "POST"])
def update_task(request, task_id):
    """
    Update an existing task.
    GET: Display form with current data
    POST: Save changes
    """
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.status = request.POST.get('status', task.status)
        
        deadline = request.POST.get('deadline')
        task.deadline = deadline if deadline else None
        
        priority_id = request.POST.get('priority_id')
        task.priority_id = priority_id if priority_id else None
        
        category_id = request.POST.get('category_id')
        task.category_id = category_id if category_id else None
        
        task.save()
        return redirect('task-detail', task_id=task.id)
    
    context = {
        'task': task,
        'priorities': Priority.objects.all().order_by('name'),
        'categories': Category.objects.all().order_by('name'),
    }
    return render(request, 'tasks/update_task.html', context)


# Delete Task View
@login_required
@require_http_methods(["GET", "POST"])
def delete_task(request, task_id):
    """
    Delete a task.
    GET: Display confirmation page
    POST: Delete the task
    """
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    
    context = {'task': task}
    return render(request, 'tasks/delete_task.html', context)


# API Views - JSON responses
@login_required
@require_http_methods(["GET"])
def task_list_api(request):
    """
    API endpoint to get all tasks as JSON.
    Optional filters: status, priority_id, category_id
    """
    tasks = Task.objects.all()
    
    # Apply filters
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)
    
    priority_id = request.GET.get('priority_id')
    if priority_id:
        tasks = tasks.filter(priority_id=priority_id)
    
    category_id = request.GET.get('category_id')
    if category_id:
        tasks = tasks.filter(category_id=category_id)
    
    tasks_list = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'deadline': task.deadline.isoformat() if task.deadline else None,
            'priority': task.priority.name if task.priority else None,
            'category': task.category.name if task.category else None,
            'created_at': task.created_at.isoformat(),
            'updated_at': task.updated_at.isoformat(),
        }
        for task in tasks
    ]
    
    return JsonResponse({'tasks': tasks_list, 'count': len(tasks_list)})


@login_required
@require_http_methods(["GET"])
def task_detail_api(request, task_id):
    """
    API endpoint to get a specific task as JSON.
    """
    task = get_object_or_404(Task, pk=task_id)
    
    task_data = {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'deadline': task.deadline.isoformat() if task.deadline else None,
        'priority': task.priority.name if task.priority else None,
        'category': task.category.name if task.category else None,
        'created_at': task.created_at.isoformat(),
        'updated_at': task.updated_at.isoformat(),
    }
    
    return JsonResponse({'task': task_data})


@login_required
@require_http_methods(["GET"])
def dashboard(request):
    """
    Dashboard view showing task statistics and summary.
    """
    total_tasks = Task.objects.count()
    pending_tasks = Task.objects.filter(status='Pending').count()
    in_progress_tasks = Task.objects.filter(status='In Progress').count()
    completed_tasks = Task.objects.filter(status='Completed').count()
    
    context = {
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'recent_tasks': Task.objects.all()[:5],
    }
    
    return render(request, 'tasks/dashboard.html', context)
