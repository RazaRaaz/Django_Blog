from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
       list_display = ["id", "owner", "title", "body", "created_time", "get_likes"]

admin.site.register(Blog, BlogAdmin) 


class CommentAdmin(admin.ModelAdmin):
       list_display = ["id", "owner", "blog", "body", "created_time"]

admin.site.register(Comment, CommentAdmin) 