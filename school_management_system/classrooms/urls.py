from rest_framework.routers import DefaultRouter
from . views import ClassroomViewSet, SubjectViewSet


router = DefaultRouter()

router.register('classrooms', ClassroomViewSet) # Register the ClassroomViewSet with the router

router.register('subjects', SubjectViewSet) # Register the SubjectViewSet with the router

urlpatterns = router.urls

