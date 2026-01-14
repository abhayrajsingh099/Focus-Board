"""
Testing Basic Features.
"""

from django.test import SimpleTestCase

from tasks.views import add


class BasicTests(SimpleTestCase):
    """Testing All Testing Features."""

    def test_addition(self):
        """Testing Addtion Fcuntion from view"""
        self.assertEqual(add(4,5), 9)