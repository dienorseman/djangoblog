from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BA
from .models import User, Categories, Post, Comment

@admin.register(User)
class Admin(BA):
    pass

@admin.register(Categories)
class AdminCategotird(admin.ModelAdmin):
    pass

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'created_at', 'published']

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['post', 'user', 'comment', 'created_at']