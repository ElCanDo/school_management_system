from django.contrib import admin
from .models import (CustomUser, 
                     Classroom, 
                     Teacher, 
                     Student, 
                     Enrollment, 
                     TeacherAssign)

admin.site.register(CustomUser)
admin.site.register(Classroom)
admin.site.register(Teacher)
admin.site.register(Student)

class EnrollmentAdmin(admin.ModelAdmin):
    model = Enrollment
    list_display = ('student', 'classroom', 'date_enrolled')
admin.site.register(Enrollment, EnrollmentAdmin)

class TeacherAssignAdmin(admin.ModelAdmin):
    model = TeacherAssign
    list_display = ('teacher', 'classroom', 'date_assigned' )
admin.site.register(TeacherAssign, TeacherAssignAdmin) 

admin.site.site_header = "School Management System"
admin.site.index_title = "Welcome To The Admin Panel"
