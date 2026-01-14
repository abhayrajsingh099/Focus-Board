"""
Test for task creation in database
"""

from django.test import TestCase

from tasks.models import Task

class TaskCreatedTest(TestCase):
    """Testing database and models behaviour."""

    def test_task_created_successful(self):
        """Test Task is created and saved in database"""
        payload = {
            'title':'Test  title',
            'description':'Hello test',
            'priority':'L',
            'is_completed':False,
        }

        task = Task.objects.create(**payload)

        data = Task.objects.filter(title=payload['title'])

        self.assertIn(task, data)
        task = Task.objects.get(title=payload['title'])
        self.assertEqual(task.title, payload['title'])
        self.assertEqual(task.description, payload['description'])
        self.assertFalse(task.is_completed)
        self.assertEqual(task.priority, payload['priority'])


    def test_default_values(self):
        """Test to know default values are correct."""
        payload = {
            'title':'Test  title',
            'description':'Hello test',
        }

        Task.objects.create(**payload)

        data = Task.objects.get(title=payload['title'])

        self.assertFalse(data.is_completed)
        self.assertEqual(data.priority, 'M')

    def test_str_of_task_model(self):
        """Test __str__() method return correctly."""
        payload = {
            'title':'Test  title',
            'description':'Hello test',
        }
        task = Task.objects.create(**payload)

        self.assertEqual(str(task), payload['title'])





