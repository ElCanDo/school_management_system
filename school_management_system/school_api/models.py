from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

"""The CustomUser Model Represents a User defined in the System, that every user inherits from"""

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]


    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    
    def save(self, *args, **kwargs):
        if self.pk:
            original_user = CustomUser.objects.get(pk=self.pk)
            if original_user.role != self.role:
                raise ValueError("user role cannot be changed")

        if self.role == 'admin':
            self.is_staff = True
            self.is_superuser = True  
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.username

    
""" The Classroom Model represents classrooms in the school with their names e.g : Grade 1 """

class Classroom(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name 
 
    
"""The Teacher Model Collects data of every Teacher employed in the School"""

class Teacher(models.Model):
   
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='teacher_profile'
    )
    full_name = models.CharField(max_length=100, null=False, blank=False)
    teacher_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) 
    subject_specialization = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_employed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.user.role if self.user else 'No role'}"
      

""" The Student Model represents Student data taken into the Sytem for storage """

class Student(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    
    full_name = models.CharField(max_length=100, null=False, blank=False, default="Unknown Student")

    date_of_birth = models.DateField(null=False, blank=False)

    mother_full_name = models.CharField(max_length=100)
    
    mother_contact = models.CharField(max_length=15, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) 
    
    father_full_name = models.CharField(max_length=100)

    father_contact = models.CharField(max_length=15,  
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')] 
        )
    home_address = models.TextField(blank=True, null=True)

    medical_allergies = models.TextField(blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    admission_date = models.DateField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.full_name} - {self.user.role if self.user else 'No role'}"   
    

"""The Enrollment model is meant to put students in their respective classrooms in the sytem"""

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='enrollments')
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'classroom')
    
    def __str__(self):
        return f"{self.student.full_name} - {self.classroom.name}"

"""The TeacherAssign model helps assign a teacher to a classroom"""

class TeacherAssign(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('teacher', 'classroom')

    def __str__(self):
        return f"{self.teacher.full_name} - {self.classroom.name}"