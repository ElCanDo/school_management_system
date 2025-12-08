from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter() # Create a router and register our viewsets with it.
router.register(r'students', StudentViewSet) # Register the StudentViewSet with the router.

urlpatterns = [
    path('', include(router.urls)),
] # Include the router URLs in the urlpatterns list.