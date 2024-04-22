from django.contrib import admin

# Register your models here.
from .models import Photo, Video, Audio, Category, Text, Article, News, NewsImage

admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Text)

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    inlines = [
        NewsImageInline,
    ]

admin.site.register(News, NewsAdmin)
admin.site.register(NewsImage)