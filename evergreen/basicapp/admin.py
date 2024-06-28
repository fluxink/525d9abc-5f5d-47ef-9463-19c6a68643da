from django.contrib import admin
from .models import Page
from image_cropping import ImageCroppingMixin



class PageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
