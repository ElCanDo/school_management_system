from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        elif user.is_superuser:
            return True

        return user.role =='admin'


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        elif user.is_superuser:
            return True

        return hasattr(user, 'teacher_profile') 
    
    
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        elif user.is_superuser:
            return True

        return hasattr(user, 'student_profile')
   