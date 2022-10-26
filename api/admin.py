from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BA
from .models import User

@admin.register(User)
class Admin(BA):
    pass
