from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, Classroom, Teacher, Student, Enrollment, TeacherAssign

User = get_user_model()


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    verify_password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    class Meta:
            model = User
            fields = ['id', 'username', 'email', 'password', 'verify_password', 
                      'role', 'first_name', 'last_name', 'tokens']
            read_only_fields = ['id', 'tokens']

    def validate(self, data):
            if data['password'] != data['verify_password']:
                raise serializers.ValidationError("Passwords must match!")
            validate_password(data['password'])
            return data 
    
    def create(self, validated_data):
        validated_data.pop('verify_password')
        password = validated_data.pop('password')

        user = User.objects.create_user(**validated_data, password=password)

        if user.role == 'teacher':
            Teacher.objects.create(user=user)
        elif user.role == 'student':
            Student.objects.create(user=user)

        return user
    

    def get_token(self, obj):
        refresh_token =RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token)
        }    
    

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']

        read_only_fields = ['id']

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name']
        read_only_field = ['id']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id', 'date_employed']

        def validate(self, user):
            if user.role != 'teacher':
                raise serializers.ValidationError("User must have role 'teacher'")
            return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'   

        read_only_fields = ['id', 'admission_date']

        def validate(self, user):
            if user.role != 'student':
                raise serializers.ValidationError("User must have role 'student'")
            return user



class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.full_name", read_only=True)
    classroom_name = serializers.CharField(source="classroom.name", read_only=True)
    class Meta:
        model = Enrollment
        fields =['id', 'student_name', 'classroom_name', 'date_enrolled' ]
        read_only_fields = ['id', 'enrollment_date']

class TeacherAssignSerializer(serializers.ModelSerializer):
    teacher_full_name = serializers.CharField(source="teacher.full_name", read_only=True)
    classroom_name = serializers.CharField(source="classroom.name", read_only=True)
    class Meta:
        model = TeacherAssign
        fields =['id', 'teacher', 'classroom']
        read_only_fields = ['id']