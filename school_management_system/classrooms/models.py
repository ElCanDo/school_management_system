from django.db import models


# Classroom model linked to Grade
class Classroom(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.grade}"    

# Subject model linked to Classroom
class Subject(models.Model):
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='subjects')
    
    def __str__(self):
        return f"{self.name} - {self.classroom.name}"    