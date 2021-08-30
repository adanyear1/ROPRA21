"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)

    def test_services(self):
        """Tests the about page."""
        response = self.client.get('/services')
        self.assertContains(response, 'services', 3, 200)

    def test_blog(self):
        """Tests the about page."""
        response = self.client.get('/blog')
        self.assertContains(response, 'blog', 3, 200)

    def test_whatisauto(self):
        """Tests the what is automation post"""
        response = self.client.get('blog/whatisautomation')
        self.assertContains(response, 'whatisautomation', 3, 200)
