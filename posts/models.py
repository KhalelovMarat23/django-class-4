from django.db import models

# Create your models here.

# def upload_post_image():


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)