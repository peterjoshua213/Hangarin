from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Priority, Category


# Priority Management Views
@login_required
@require_http_methods(["GET"])
def priority_list(request):
    """
    Display all priorities for the logged-in user.
    """
    priorities = Priority.objects.filter(user=request.user).order_by('name')
    context = {
        'priorities': priorities,
    }
    return render(request, 'tasks/priority_list.html', context)


@login_required
@require_http_methods(["POST"])
def create_priority(request):
    """
    Create a new priority for the logged-in user.
    """
    name = request.POST.get('name', '').strip()
    
    if not name:
        return JsonResponse({'error': 'Priority name is required'}, status=400)
    
    # Check if priority already exists for this user
    if Priority.objects.filter(user=request.user, name=name).exists():
        return JsonResponse({'error': 'Priority already exists'}, status=400)
    
    priority = Priority.objects.create(user=request.user, name=name)
    
    return JsonResponse({
        'id': priority.id,
        'name': priority.name,
        'message': 'Priority created successfully'
    })


@login_required
@require_http_methods(["POST"])
def update_priority(request, priority_id):
    """
    Update a priority.
    """
    priority = get_object_or_404(Priority, pk=priority_id, user=request.user)
    name = request.POST.get('name', '').strip()
    
    if not name:
        return JsonResponse({'error': 'Priority name is required'}, status=400)
    
    priority.name = name
    priority.save()
    
    return JsonResponse({
        'id': priority.id,
        'name': priority.name,
        'message': 'Priority updated successfully'
    })


@login_required
@require_http_methods(["POST", "DELETE"])
def delete_priority(request, priority_id):
    """
    Delete a priority.
    """
    priority = get_object_or_404(Priority, pk=priority_id, user=request.user)
    priority.delete()
    
    return JsonResponse({'message': 'Priority deleted successfully'})


# Category Management Views
@login_required
@require_http_methods(["GET"])
def category_list(request):
    """
    Display all categories for the logged-in user.
    """
    categories = Category.objects.filter(user=request.user).order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, 'tasks/category_list.html', context)


@login_required
@require_http_methods(["POST"])
def create_category(request):
    """
    Create a new category for the logged-in user.
    """
    name = request.POST.get('name', '').strip()
    
    if not name:
        return JsonResponse({'error': 'Category name is required'}, status=400)
    
    # Check if category already exists for this user
    if Category.objects.filter(user=request.user, name=name).exists():
        return JsonResponse({'error': 'Category already exists'}, status=400)
    
    category = Category.objects.create(user=request.user, name=name)
    
    return JsonResponse({
        'id': category.id,
        'name': category.name,
        'message': 'Category created successfully'
    })


@login_required
@require_http_methods(["POST"])
def update_category(request, category_id):
    """
    Update a category.
    """
    category = get_object_or_404(Category, pk=category_id, user=request.user)
    name = request.POST.get('name', '').strip()
    
    if not name:
        return JsonResponse({'error': 'Category name is required'}, status=400)
    
    category.name = name
    category.save()
    
    return JsonResponse({
        'id': category.id,
        'name': category.name,
        'message': 'Category updated successfully'
    })


@login_required
@require_http_methods(["POST", "DELETE"])
def delete_category(request, category_id):
    """
    Delete a category.
    """
    category = get_object_or_404(Category, pk=category_id, user=request.user)
    category.delete()
    
    return JsonResponse({'message': 'Category deleted successfully'})
