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
    date_of_birth = serializers.DateField(write_only=True, required=False)
    class Meta:
            model = User
            fields = ['id', 'username', 'email', 'password', 'verify_password',  'first_name', 'last_name', 'date_of_birth', 'role', 'tokens']
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
        date_of_birth = validated_data.get('date_of_birth')


        if user.role == 'teacher':
            Teacher.objects.create(user=user, full_name=f"{user.first_name} {user.last_name}".strip())
        elif user.role == 'student':
            Student.objects.create(user=user, full_name=f"{user.first_name} {user.last_name}".strip(), date_of_birth=date_of_birth)
        else:
            raise serializers.ValidationError('User role must be specified')
        return user
    

    def get_tokens(self, obj):
        refresh =RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }    
    

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']

        read_only_fields = ['id', 'role']

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

    def validate_user(self, value):
        if value.role != 'teacher':
            raise serializers.ValidationError("User must have role 'teacher'")
        return value


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'   

        read_only_fields = ['id', 'admission_date']

    def validate_user(self, value):
        if value.role != 'student':
            raise serializers.ValidationError("User must have role 'student'")
        return value



class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.full_name', read_only=True)
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)
    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['id', 'date_enrolled']


class TeacherAssignSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.full_name', read_only=True)
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)
    class Meta:
        model = TeacherAssign
        fields =['id', 'teacher', 'classroom','teacher_name', 'classroom_name']
        read_only_fields = ['id']
