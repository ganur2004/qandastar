from django.contrib import admin

# Register your models here.
from .models import Photo, Video, Audio

admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Audio)