from django.test import TestCase
from .models import Photo, Category, Location


# Testcase for Photo class
class TestPhoto(TestCase):
    def setUp(self):
        self.category = Category(name='travel')
        self.category.save_category()

        self.location = Location(name='dubai')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Photo))

    def test_save_image(self):
        self.save_image()
        stored = Photo.objects.all()
        self.assertTrue(len(stored) > 0)

    def test_delete_image(self):
        self.delete_image()
        images = Photo.objects.all()
        self.assertTrue(len(images) == 0)

    def tearDown(self):
        Photo.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

# Testcase for Category class
class TestCategory(TestCase):
    def setUp(self):
        self.category = Category(name='travel')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

# Testcase for Location class
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='dubai')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


