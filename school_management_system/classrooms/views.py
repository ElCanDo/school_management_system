from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Classroom, Subject
from .serializers import ClassroomSerializer, SubjectSerializer # type: ignore

#Viewsets for Classroom and Subject 

class ClassroomViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer    

