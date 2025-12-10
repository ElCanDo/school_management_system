from django.db import models # Importing models module from django.db
from django.core.validators import RegexValidator # RegexValidator for validating phone numbers

# Student model definition
class Student(models.Model):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]# Choices for gender field

    # Inheritting from custom user model defined in 'accounts' app
    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='student_profile'
    )#Link Student to CustomUser model

    date_of_birth = models.DateField()# Date of birth of the student
    mother_full_name = models.CharField(max_length=200)# Full name of the mother
    
    mother_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) # Validates phone number format
    
    father_full_name = models.CharField(max_length=200)# Full name of the father
    father_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')] # Validates phone number format
        )
    home_address = models.TextField()# Student's residential address
    medical_allergies = models.TextField()# Any known medical allergies
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)# Gender of the student
    enrollment_date = models.DateField(auto_now_add=True)# Date when the student was enrolled
    grade = models.ForeignKey('classrooms.classroom', on_delete=models.SET_NULL, null=True, related_name='students')# Grade level of the student

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - ({self.role})"