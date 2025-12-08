from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer

#Student ViewSet for CRUD operations
class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] # Use TokenAuthentication for authentication
    permission_classes = [IsAuthenticated] # Require users to be authenticated
    queryset = Student.objects.all() # Get all Student objects
    serializer_class = StudentSerializer # Use StudentSerializer for serialization