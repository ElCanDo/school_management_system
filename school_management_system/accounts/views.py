from django.shortcuts import render
from . models import CustomUser
from . serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# CustomUser ViewSet for CRUD operations
class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all() # Get all CustomUser objects
    serializer_class = CustomUserSerializer() # Use CustomUserSerializer for serialization
    