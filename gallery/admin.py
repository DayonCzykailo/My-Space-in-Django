from django.contrib import admin
from gallery.models import Photo

class Photos(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'image')
    list_per_page = 8

admin.site.register(Photo, Photos)
