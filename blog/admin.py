from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models import Blog, Author


class BlogAdmin(ModelAdmin):
    list_display = ('id', 'name', 'content')


class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'name', 'email')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
