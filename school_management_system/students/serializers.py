from rest_framework import serializers
from accounts.serializers import CustomUserSerializer 
from .models import Student

# Serializer for the Student model
class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Nested serializer for the related CustomUser model

    class Meta:
        model = Student
        fields = [
            'date_of_birth',
            'mother_full_name',
            'mother_contact',
            'father_full_name',
            'father_contact',
            'home_address',
            'medical_allergies',
            'gender',
            'enrollment_date',
            'grade',
        ]   # Fields to be included in the serialization
         
        read_only_fields = ['enrollment_date']  # enrollment_date is read-only