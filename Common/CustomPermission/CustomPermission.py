from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
