import os
from .models import Task, Tag
from celery import shared_task
from django.core.mail import send_mail

def create_task(title, description, completed, due_date, image, selected_tags_ids):
    if due_date:
        new_task = Task.objects.create(
            title=title,
            description=description,
            completed=completed,
            due_date=due_date,
            image=image
        )
    else:
        new_task = Task.objects.create(
            title=title,
            description=description,
            completed=completed,
            image=image
        )

    for tag_id in selected_tags_ids:
        tag = Tag.objects.get(id=tag_id)
        new_task.tags.add(tag)

    return new_task

def update_task(task, title, description, completed, due_date, image, selected_tags_ids):
    if due_date:
        task.due_date = due_date

    if image:
        task.image = image

    task.title = title
    task.description = description
    task.completed = completed
    task.save()

    task.tags.clear()
    for tag_id in selected_tags_ids:
        tag = Tag.objects.get(id=tag_id)
        task.tags.add(tag)

    return task

def delete_task(task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()

@shared_task
def send_task_creation_email(task_id):
    task = Task.objects.get(pk=task_id)
    send_mail(
        'Nouvelle tâche créée',
        f'La tâche "{task.title}" a été créée avec succès!',
        os.getenv('EMAIL_HOST_USER'),
        ['mkaddemhaykel@gmail.com'],
        fail_silently=False,
    )