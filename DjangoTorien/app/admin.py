from django.contrib import admin
from django import forms
from app.models import *

admin.site.register(Gallery)
admin.site.register(Collection)
admin.site.register(Category)

class GalleryInline(admin.TabularInline):
    fk_name = 'thing'
    model = Gallery


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    formfield_overrides = {
        fields.ColorField: {'widget': forms.TextInput(attrs={'type': 'color', \
            'style': 'height: 100px; width: 100px;'})}
    }