from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('zakaz', zakaz, name='zakaz'),
    path('services', services, name='services'),
    path('get-a-quote', get_a_quote, name='get-a-quote'),
]