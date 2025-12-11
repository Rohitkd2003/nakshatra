from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "Admin"


class IsDoctorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ["Doctor", "Admin"]
