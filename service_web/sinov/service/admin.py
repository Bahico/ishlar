from .models import Task
from django.contrib import admin


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo']


admin.site.register(Task, TaskAdmin)
