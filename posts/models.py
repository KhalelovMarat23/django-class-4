from django.db import models

# Create your models here.

# def upload_post_image():


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='posts', blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    mark = models.IntegerField(default=5)
