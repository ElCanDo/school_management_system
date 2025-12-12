from rest_framework import serializers
from accounts.serializers import CustomUserSerializer 
from .models import Student

# Serializer for the Student model
class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True) 

    class Meta:
        model = Student
        fields = '__all__'   

        read_only_fields = ['enrollment_date']  