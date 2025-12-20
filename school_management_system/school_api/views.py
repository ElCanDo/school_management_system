from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.response import Response
from django.shortcuts import redirect
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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()

        return Response(
            {
"message": "User successfully registered",
"user": CustomUserSerializer(user).data,
"token" : serializer.get_tokens(user)
},
      status=status.HTTP_201_CREATED
)


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


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer
    permission_classes = [IsAdmin, IsStudent]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdmin, IsTeacher]
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_name', 'classroom_name']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()

        return Response(
            {
"message": f"Pupil {serializer.data['student_name']} is successfully enrolled into {serializer.data['classroom_name']}",
"data": serializer.data
},
      status=status.HTTP_201_CREATED
)
    



class TeacherAssignViewSet(viewsets.ModelViewSet):
    queryset = TeacherAssign.objects.all()
    serializer_class = TeacherAssignSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['teacher_full_name', 'classroom_name']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()

        return Response(
            {
"message": f"Madam/Sir {serializer.data['teacher_name']} is successfully assigned to {serializer.data['classroom_name']}",
"data": serializer.data
},
      status=status.HTTP_201_CREATED
)
