from django.db import models 
from django.core.validators import RegexValidator 

# Student model definition
class Student(models.Model):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    
    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    
    full_name = models.CharField(max_length=200, null=False, blank=False, default='Unknown student')

    date_of_birth = models.DateField()

    mother_full_name = models.CharField(max_length=200)
    
    mother_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) 
    
    father_full_name = models.CharField(max_length=200)

    father_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')] 
        )
    home_address = models.TextField(blank=True, null=True)

    medical_allergies = models.TextField(blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    enrollment_date = models.DateField(auto_now_add=True)

    grade = models.ForeignKey('classrooms.Classroom', on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f"{self.full_name} - Student"