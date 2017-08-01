from django.contrib import admin

from .models import TfPics, TfRoles, TfToys, TfStory

admin.site.register(TfPics)
admin.site.register(TfRoles)
admin.site.register(TfToys)
admin.site.register(TfStory)