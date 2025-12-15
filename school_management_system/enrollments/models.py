from django.db import models
from students.models import Student
from classrooms.models import Classroom


class Enrollment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='students_enrolled')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroom_enrollments')
    date_enrolled = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.student.full_name} - {self.classroom.name}"