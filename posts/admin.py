from django.contrib import admin
from posts import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)