from django.contrib import admin
from .models import Category, Tag, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary', 'body', 'views', 'create_time', 'modeified_time', 'category', 'author',]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)