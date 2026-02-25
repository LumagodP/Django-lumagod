from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status_badge', 'due_date', 'created_at')
    list_filter = ('status', 'created_at', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_editable = ()
    date_hierarchy = 'created_at'
    list_per_page = 10

    def status_badge(self, obj):
        colors = {
            'pending': 'orange',
            'in_progress': 'blue',
            'completed': 'green',
        }
        color = colors.get(obj.status, 'gray')
        return format_html(
            '<strong style="color: {};">{}</strong>',
            color,
            obj.get_status_display()
        )

    status_badge.short_description = 'Status'

from django.utils.html import format_html