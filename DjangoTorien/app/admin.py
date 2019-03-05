from django.contrib import admin
from django import forms
from app.models import *

admin.site.register(Size)
admin.site.register(Gallery)
admin.site.register(Collection)
admin.site.register(Category)
#admin.site.register(Thing)
admin.site.register(Color)

class GalleryInline(admin.TabularInline):
    fk_name = 'thing'
    model = Gallery
    
#class SizeInline(admin.TabularInline):
#    fk_name = 'thing'
#    model = Size


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    #formfield_overrides = {
    #    fields.ColorField: {'widget': forms.TextInput(attrs={'type': 'color', \
    #        'style': 'height: 100px; width: 100px;'})}
    #}