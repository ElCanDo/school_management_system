from django.contrib import admin
from .models import Student

# Student Admin Configuration
class StudentAdmin(admin.ModelAdmin):# Custom admin configuration for Student model
    list_display = ("name", "age", "enrollment_date", "gender", "grade") # Fields to display in admin list view
    search_fields = ("name", "grade") # Fields to search in admin

admin.site.register(Student, admin.ModelAdmin) # Registering Student model with custom admin configuration