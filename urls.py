from django.conf.urls import url
from django.contrib import admin

from .import views
from .views import *
from.import views

app_name='API'

urlpatterns = [
    url(r'index/$',index,),
    url(r'update_location/', update_location),
    url(r'image_Save/',image_Save),
    url(r'getLocation/', getLocation),
    ]