from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CustomUserRegistrationView, CustomUserViewSet, 
                    ClassroomViewSet, 
                    TeacherViewSet, 
                    StudentViewSet, 
                    EnrollmentViewSet,
                    TeacherAssignViewSet)

router = DefaultRouter() 
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'teacher-assignments', TeacherAssignViewSet, basename='teacher-assignment')

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('register/', CustomUserRegistrationView.as_view(), name='registration'),

]