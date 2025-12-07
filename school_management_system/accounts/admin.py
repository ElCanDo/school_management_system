from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email', 'role')
    list_filter = ('role', )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
admin.site.register(CustomUser, CustomUserAdmin)
