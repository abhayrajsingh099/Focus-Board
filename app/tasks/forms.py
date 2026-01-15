"""
Froms for Task App
"""

from django import forms

from tasks.models import Task

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description',
            'priority', 'is_completed'
        ]
        help_texts = {'title' : 'Enter a Task to do...'}



