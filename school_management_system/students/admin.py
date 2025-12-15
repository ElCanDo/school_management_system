from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "gender", "age", "enrollment_date", "grade") 
    
    search_fields = ("Full_name", "mother_full_name", "father_full_name")

admin.site.register(Student, StudentAdmin) 