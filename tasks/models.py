from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)

class Tag(models.Model):
    title = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task, related_name='tags')
