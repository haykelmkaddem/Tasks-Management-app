from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .services import create_task, update_task, delete_task, send_task_creation_email


def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        due_date = request.POST.get('due_date')
        image = request.FILES.get('image')
        selected_tags_ids = request.POST.getlist('tags')
        new_task = create_task(title, description, completed, due_date, image, selected_tags_ids)
        send_task_creation_email.delay(new_task.id)
        return redirect('task-list')

    tags = Tag.objects.all()
    return render(request, 'tasks/create_task.html', {'tags': tags})

def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        due_date = request.POST.get('due_date')
        image = request.FILES.get('image')
        selected_tags_ids = request.POST.getlist('tags')

        update_task(task, title, description, completed, due_date, image, selected_tags_ids)
        return redirect('task-list')

    tags = Tag.objects.all()
    return render(request, 'tasks/update_task.html', {'task': task, 'tags': tags})



def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/list_task.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_delete(request, task_id):
    if request.method == 'POST':
        delete_task(task_id)
        return redirect('task-list')