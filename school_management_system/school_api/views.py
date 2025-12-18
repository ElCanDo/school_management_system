from rest_framework import viewsets, permissions, filters, generics
from .serializers import (CustomUserRegistrationSerializer, 
                          CustomUserSerializer, 
                           ClassroomSerializer, 
                           TeacherSerializer, 
                           StudentSerializer, 
                           EnrollmentSerializer, 
                           TeacherAssignSerializer)
from .models import CustomUser, Classroom, Teacher, Student, Enrollment, TeacherAssign
from .permissions import IsAdmin, IsTeacher, IsStudent


"""Viewsets For all the Models"""

class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationSerializer
    permission_classes  = [permissions.AllowAny]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'role']


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin, IsTeacher]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'subject_specialization']

    def get_object(self):
        return self.request.user.teacher_profile


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer
    permission_classes = [IsAdmin, IsStudent]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

    def get_object(self):
        return self.request.user.student_profile


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdmin, IsTeacher]
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_full_name', 'classroom_name']


class TeacherAssignViewSet(viewsets.ModelViewSet):
    queryset = TeacherAssign.objects.all()
    serializer_class = TeacherAssignSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['teacher_full_name', 'classroom_name']