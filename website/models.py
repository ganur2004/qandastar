from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    nameImage = models.CharField(max_length=100, blank=True)
    descriptionImage = models.CharField(max_length=500, blank=True)
    categoryImage = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    dateOfImage = models.DateField(blank=True, null=True)
    uploadDateImage = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')
    nameVideo = models.CharField(max_length=100, blank=True)
    descriptionVideo = models.CharField(max_length=500, blank=True)
    categoryVideo = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    dateOfVideo= models.DateField(blank=True, null=True)
    uploadDateVideo = models.DateTimeField(auto_now_add=True)

class Audio(models.Model):
    audio_file = models.FileField(upload_to='audios/')
    nameAudio = models.CharField(max_length=100, blank=True)
    descriptionAudio = models.CharField(max_length=500, blank=True)
    categoryAudio = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    dateOfAudio = models.DateField(blank=True, null=True)
    uploadDateAudio = models.DateTimeField(auto_now_add=True)