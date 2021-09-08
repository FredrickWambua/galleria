from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt



# Photo class model
class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    # Photo model methods
    def desc(self):
        return self.description[:150]+' ...'

    def publish_date(self):
        return self.pub_date.strftime('%Y-%m-%d')

    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete()

    def update_image(self):
        return self.update_image()

    @classmethod
    def get_image_by_id(cls):
        got_image = cls.objects.get(pk=id)
        return got_image

    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains = search_term)
        return images
    @classmethod
    def filter_by_location(cls):
        locality = cls.objects.filter('location')
        return locality
    
    def __str__(self):
        return self.description


# Category class model for the photos
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    # save, delete and update methods for a category
    def save_category(self):
        return self.save()

    def delete_category(self):
        return self.delete()

    def update_category(self):
        return self.update_category()




# Location class method
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
    def __str__(self):
        return self.name

    # save, delete and update methods for location
    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    def update_location(self):
        return self.update_location()