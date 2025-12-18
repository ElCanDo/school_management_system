from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and 
                request.user.role =='admin'
                )
    

# class IsTeacher(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and not request.user.is_staff

#     def has_object_permission(self, request, view, obj):
#         return True


# class IsStudent(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and not request.user.is_staff
    
#     def has_object_permission(self, request, view, obj):
#         return True
    
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'student_profile')

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'teacher_profile')    