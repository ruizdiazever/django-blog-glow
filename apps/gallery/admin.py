from django.contrib import admin
from django.contrib import admin
from django.contrib import admin

# Register your models here.
from .models import Photo
from .models import Ba
from .models import Industrial
from .models import People

# BARILOCHE
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Photo, PhotoAdmin)

#BUENOS AIRES
class BaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Ba, BaAdmin)

#Industrial
class IndustrialAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Industrial, IndustrialAdmin)

#People
class PeopleAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(People, PeopleAdmin)
