from django.shortcuts import render

from .models import Photo
from .models import Ba
from .models import People
from .models import Industrial

def mountain(request):
    photos = Photo.objects.all()
    return render(request, "gallery/mountain.html", {'photos':photos})

def ba(request):
    ba = Ba.objects.all()
    return render(request, "gallery/ba.html", {'ba':ba})

def people(request):
    people = People.objects.all()
    return render(request, "gallery/people.html", {'people':people})

def industrial(request):
    industrial = Industrial.objects.all()
    return render(request, "gallery/industrial.html", {'industrial':industrial})