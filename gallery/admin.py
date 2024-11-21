from django.contrib import admin
from gallery.models import Photo

class Photos(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'image')


admin.site.register(Photo, Photos)
