from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Task

from .utils import has_ASCII


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'priority']

    # def validate_description(self, description):
    #     """Description can't be just empty."""
    #     if not has_ASCII(description):
    #         raise ValidationError("description can't be empty or Just whitespaces.")

    #     return description

    def validate(self, task):
        """Task completed must have description."""
        try:
            description = task['description']
        except Exception:
            description = self.instance.description

        if task['is_completed'] and not has_ASCII(description):
            raise ValidationError("A completed task must have a description.")

        return task


