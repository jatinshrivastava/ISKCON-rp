from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'phone_number', 'first_name', 'last_name', 'gender']
    fieldsets = (
        ("Credentials", {'fields': (
            'username', 'password')}),
        ("Basic Details", {'fields': (
            'first_name', 'last_name', 'email', 'gender', 'birth_date', 'address',
            'date_joined')}),
        ("Permissions", {'fields': ('user_permissions',)}),
    )
    pass


admin.site.register(CustomUser, CustomUserAdmin)
