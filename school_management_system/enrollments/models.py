from django.db import models
from students.models import Student
from classrooms.models import Classroom


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_enrollments')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroom_enrollments')
