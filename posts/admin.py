from django.contrib import admin
from posts import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    filter_horizontal = ('tag', )
    list_filter = ('category', )
    search_fields = ('title', 'description')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)