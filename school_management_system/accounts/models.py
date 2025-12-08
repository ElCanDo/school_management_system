from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model extending AbstractUser
class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser with unique email and role fields.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ] # Choices for user roles
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email'] 

    def __str__(self):
        return f"{self.username} ({self.role})"

