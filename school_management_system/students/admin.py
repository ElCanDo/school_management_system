from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "age", "enrollment_date", "gender", "grade") 
    search_fields = ("Full_name", "grade") 

admin.site.register(Student, StudentAdmin) 