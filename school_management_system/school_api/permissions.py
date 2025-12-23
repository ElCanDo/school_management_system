from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        elif user.is_superuser:
            return True

        return user.role =='admin'


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        elif user.is_superuser:
            return True

        return hasattr(user, 'teacher_profile') 
    
    
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        elif user.is_superuser:
            return True

        return hasattr(user, 'student_profile')
   