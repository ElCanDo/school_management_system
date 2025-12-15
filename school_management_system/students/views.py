from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAdminUser
from .models import Student
from .serializers import StudentSerializer

#Student ViewSet for CRUD operations
class StudentViewSet(viewsets.ModelViewSet):
    """"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Student.objects.select_related('user', 'grade').all() 
    serializer_class = StudentSerializer


    # def get_queryset(self):
    #     user = self.request.user
    #     if user.role == "Student":
    #         return Student.objects.filter(user=user)
    #     return super().get_queryset()