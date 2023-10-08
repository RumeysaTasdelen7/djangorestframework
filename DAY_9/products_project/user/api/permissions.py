from rest_framework import permissions


class IsRequestUserPermissons(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.pk == obj.pk)