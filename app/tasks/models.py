"""
Model for Tasks
"""
from django.db import models

PRIORITY = [
    ('L', 'low'),
    ('M', 'medium'),
    ('H', 'high'),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY,
        default="Medium",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



