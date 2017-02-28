from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.galleries.admin import GalleryAdmin, GalleryImageInline
from mezzanine.galleries.models import Gallery
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, VideoURL

# Register your models here.
class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class VideoInline(TabularDynamicInlineAdmin):
    model = VideoURL
#class IconInline(TabularDynamicInlineAdmin):
#    model = IconBlurb

class HomePageAdmin(PageAdmin):
    model = HomePage
    inlines = [
        SlideInline,
    ]

class MyGalleryAdmin(GalleryAdmin):
    inlines = [
        VideoInline, GalleryImageInline
    ]

admin.site.unregister(Gallery)
admin.site.register(Gallery, MyGalleryAdmin)
admin.site.register(HomePage, HomePageAdmin)
