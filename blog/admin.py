from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
       list_display = ["id", "owner", "title", "body", "created_time", "get_likes"]

admin.site.register(Blog, BlogAdmin) 