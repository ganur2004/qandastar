from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')

class Audio(models.Model):
    audio_file = models.FileField(upload_to='audios/')