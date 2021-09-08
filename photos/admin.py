from django.contrib import admin
from django.db import models
from .models import Photo, Category, Location

# Register your models here.
models = (Photo, Category, Location)

for model in models:
    if model == 'Category':
        admin.site.register(Category,'CategoryAdmin')
    else:
        admin.site.register(model)
class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('location')