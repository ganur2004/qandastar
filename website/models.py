from django.db import models
import PyPDF2, docx2txt, os

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

class Text(models.Model):
    key = models.CharField(max_length=100, unique=True)
    content_kz = models.TextField()
    content_ru = models.TextField()

class Article(models.Model):
    article_file = models.FileField(upload_to='article/')
    nameArticle = models.CharField(max_length=100, blank=True)
    partArticle = models.TextField(blank=True)
    categoryArticle = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    dateOfAudio = models.DateField(blank=True, null=True)
    uploadDateAudio = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.article_file:
            self.partArticle = self.extract_text_from_file(self.article_file.path)
        super().save(*args, **kwargs)

    def extract_text_from_file(self, file_path):
        if os.path.exists(file_path):
            file_extension = file_path.split('.')[-1].lower()
            if file_extension == 'pdf':
                with open(file_path, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    first_page = pdf_reader.pages[0]
                    return first_page.extract_text()
            elif file_extension == 'docx':
                return docx2txt.process(file_path)
            else:
                return 'Формат файла не поддерживается'
        else:
            return 'Файл не найден'
