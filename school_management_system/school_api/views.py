from rest_framework import viewsets, permissions
from .serializers import (CustomUserSerializer, 
                           ClassroomSerializer, 
                           TeacherSerializer, 
                           StudentSerializer, 
                           EnrollmentSerializer, 
                           TeacherAssignSerializer)
from .models import CustomUser, Classroom, Teacher, Student, Enrollment, TeacherAssign

"""Viewsets For all the Models"""

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [permissions.IsAdminUser]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAdminUser]

class TeacherAssignViewSet(viewsets.ModelViewSet):
    queryset = TeacherAssign.objects.all()
    serializer_class = TeacherAssignSerializer
    permission_classes = [permissions.IsAdminUser]