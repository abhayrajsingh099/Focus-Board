"""
Admin configuration for Task model
"""

from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    ordering = ('-priority', '-created_at')
    # lists the data of a Model
    list_display = ('title', 'priority', 'is_completed', 'created_at')
    list_filter = ('created_at', 'priority', 'is_completed')
    list_editable = ('is_completed', 'priority')
    date_hierarchy = 'created_at'


    # Controlling which fields are displayed and laid out inside the Form (+ADD Model)
        # M-1
    # fields = ['title', 'description',
    #     ('is_completed', 'priority'),
    #     'created_at',
    # ]
        # M-2 Sectioning the detail view
    fieldsets = (
        (None, {
            'fields':('title', 'description')
        }),
        ('Status & Priority',{
            'fields':(('is_completed', 'priority'),)
        }),
    )


    readonly_fields = ['created_at']

