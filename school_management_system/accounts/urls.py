from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter() # Create a router and register our viewsets with it.
router.register(r'accounts', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
] # Include the router URLs in the urlpatterns list.