from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import GradeViewSet, ClassroomViewSet, SubjectViewSet


router = DefaultRouter()
router.register(r'grade', GradeViewSet) # Register the GradeViewzSet with the router

router.register(r'classrooms', ClassroomViewSet) # Register the ClassroomViewSet with the router

router.register(r'subjects', SubjectViewSet) # Register the SubjectViewSet with the router

urlpatterns = [
    path('', include(router.urls))
] # Include the router URLs in the pattern list
