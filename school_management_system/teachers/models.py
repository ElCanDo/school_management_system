from django.db import models
from django.core.validators import RegexValidator


# Teacher model representing school teachers
class Teacher(models.Model):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='teacher_profile'
    )
    full_name = models.CharField(max_length=200, null=False, blank=False, default='Unknown teacher')
    teacher_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) 
    
    subject_specialization = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_hired = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"