from django.db import models
from teachers.models import Teacher

""" Classroom model """

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, related_name="classroom")

    class Meta:
        unique_together = ('name', 'grade')

    def __str__(self):
        return f"{self.name} - Grade {self.grade}"    


"""Subject for a Classroom"""

class Subject(models.Model):
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='subjects')
    
    class Meta:
        unique_together = ('name', 'classroom')

    def __str__(self):
        return f"{self.name} - {self.classroom}"    