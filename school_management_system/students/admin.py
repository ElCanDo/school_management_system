from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

# Student Admin Configuration
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "enrollment_date", "gender", "grade") 

admin.site.register(Student, UserAdmin) 