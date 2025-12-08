from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# CustomUser Admin Configuration
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('first_name', 
                    'last_name', 
                    'email', 
                    'role') # Fields to display in admin list view
    
    list_filter = ('role', ) # Filter by role in admin

    search_fields = ('username',
                      'email', 
                      'first_name', 
                      'last_name') # Fields to search in admin
    
    ordering = ('username',) # Default ordering in admin

# Registering CustomUser model with CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin) 
