from django.contrib import admin
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path('mountain', views.mountain, name='mountain'),
    path('buenosaires', views.ba, name='ba'),
    path('people', views.people, name='people'),
    path('industrial', views.industrial, name='industrial'),
]