from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_data', 'priority', 'completed', 'is_overdue']
    list_filter = ['priority', 'completed', 'due_data']
    search_fields = ['title', 'priority']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']

    def is_overdue(self, obj):
        return obj.is_overdue()
    is_overdue.boolean = True
    is_overdue.short_description = 'Atrasada'

admin.site.register(Task, TaskAdmin)
