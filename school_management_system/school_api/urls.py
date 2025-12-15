from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CustomUserViewSet, 
                    ClassroomViewSet, 
                    TeacherViewSet, 
                    StudentViewSet, 
                    EnrollmentViewSet,
                    TeacherAssignViewSet)

router = DefaultRouter() 
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'teachers', TeacherViewSet, bassname='teacher')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'teacher-assignments', TeacherAssignViewSet, basename='teacher-assignment')

urlpatterns = [
    path('', include(router.urls)),
]