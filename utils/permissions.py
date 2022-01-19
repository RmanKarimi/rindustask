from django.utils.translation import gettext_lazy as _
from rest_framework import permissions


class AllowOwner(permissions.BasePermission):
    message = _('You are not the owner.')

    def has_object_permission(self, request, view, obj):
        if not (request.user and request.user.is_authenticated):
            return False

        user = request.user
        if obj.user_id == user.pk:
            return True
        return False


class AllowAdminAndOwner(permissions.BasePermission):
    message = _('You are neither admin or owner.')

    def has_object_permission(self, request, view, obj):
        print('================================')
        print('================================')
        if not (request.user and request.user.is_authenticated):
            return False

        user = request.user
        if obj.id == user.pk and user.is_superuser:
            return True
        return False

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser