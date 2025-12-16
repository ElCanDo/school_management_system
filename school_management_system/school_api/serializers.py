from rest_framework import serializers
from .models import CustomUser, Classroom, Teacher, Student, Enrollment, TeacherAssign

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
        read_only_fields = ['id']

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name']



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_field = ['id', 'date_employed']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'   

        read_only_fields = ['id', 'enrollment_date']

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.full_name", read_only=True)
    class_name = serializers.CharField(source="classroom.name", read_only=True)
    class Meta:
        model = Enrollment
        fields =['id', 'student_name', 'classroom_name', 'date_enrolled' ]
        read_only_field = ['id']

class TeacherAssignSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="teacher.full_name", read_only=True)
    class_name = serializers.CharField(source="classroom.name", read_only=True)
    class Meta:
        model = TeacherAssign
        fields =['id', 'teacher_full_name', 'classroom_name']
        read_only_field= ['id']