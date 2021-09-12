from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.conf.urls.static import static
import photos
from django.conf import settings


urlpatterns=[
    url('^$', views.index, name='home'),
    url('^travel', views.travel, name='travel'),
    url('^culture', views.culture, name = 'culture'),
    url('^sports', views.sports, name = 'sports'),
    url('^search', views.search, name= 'search'),
    path('photodetails/<int:pk>/',views.view_photo, name='picha'),
    # path('^location/(?P<location>\w+)/', views.image_location, name='location'),

]
