from django.shortcuts import render
from .models import Photo, Video, Audio


# Create your views here.
def main(request):
    latest_photos = Photo.objects.order_by('-id')[:10]
    latest_audios = Audio.objects.order_by('-id')[:4]
    latest_videos = Video.objects.order_by('-id')[:3]
    return render(request, 'main.html', {'latest_photos': latest_photos, 'latest_audios': latest_audios, 'latest_videos': latest_videos})


def photo_view(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos': photos})

def video_view(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos})

def audio_view(request):
    audios = Audio.objects.all()
    return render(request, 'audios.html', {'audios': audios})

def photos_html_view(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos': photos})

def suhbat_html_view(request):
    videos = Video.objects.all()
    audios = Audio.objects.all()
    return render(request, 'suhbat.html', {'videos': videos, 'audios': audios})