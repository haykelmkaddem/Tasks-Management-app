from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'due_date')
    list_filter = ('completed', 'due_date')
    search_fields = ('title', 'description')
    list_per_page = 10

admin.site.register(Task, TaskAdmin)
