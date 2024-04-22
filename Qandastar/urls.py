"""Qandastar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static
from website.views import text_view, change_language



urlpatterns = [
    path('', views.main, name='main'),
    path('main.html', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('photos/', views.photo_view, name='photo_view'),
    path('videos/', views.video_view, name='video_view'),
    path('audios/', views.audio_view, name='audio_view'),
    path('article.html', views.article_view, name='article_view'),
    path('photos.html', views.photos_html_view, name='photos_html_view'),
    path('suhbat.html', views.suhbat_html_view, name='suhbat_html_view'),  
    path('text/<str:key>/', text_view, name='text_view'),
    path('change_language/', change_language, name='change_language'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)