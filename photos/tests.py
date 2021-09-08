from django.test import TestCase
from .models import Photo, Category, Location

# Create your tests here.

class TestPhoto(TestCase):
    def setUp(self):
        self.category = Category(name='travel')
        self.category.save_category()

        self.location = Location(name='dubai')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Photo))


