from django.db.models import query
import photos
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Photo, Category , Location
from django.db.models import Q

# Create your views here.
def index(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()  
    context = {'categories': categories, 'photos':photos}
    return render(request, 'galleria/index.html', context)

def view_photo(request, pk):
    view_photo = Photo.objects.get(id=pk)
    return render(request, 'galleria/photodetails.html', {'view_photo': view_photo })

def travel(request):
    travel_cat = Category.objects.all()
    travel = Photo.objects.filter(travel_cat)
    return render(request, 'galleria/travel.html', {'travel':travel})

def culture(request):
    culture_cat = Category.objects.all()
    culture = Photo.objects.filter(culture_cat)
    return render(request, 'galleria/culture.html', {'culture':culture})

def sports(request):
    sports_cat = Category.objects.all()
    sports = Photo.objects.filter(sports_cat)
    return render(request, 'galleria/sports.html', {'sports':sports})

def image_location(request, location):
    photos = Photo.filter_by_location(location)
    return render(request, 'galleria/location.html', {'location_images': photos})

def search(request):
    if request.method=='GET':
        result = request.GET.get('q')
        if result:
            display = Photo.objects.filter(Q(name__icontains = result)|Q(location__name__icontains = result)|Q(category__name__icontains = result))
            print(display)
            return render(request, 'galleria/search.html', {'display': display})
        else:
            message = "No information found from your search. Try to refine your search term"
            return render(request, 'galleria/search.html',{"message":message})

