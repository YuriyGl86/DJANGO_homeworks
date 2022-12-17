from rest_framework.permissions import BasePermission


class IsOwnerOrAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or request.user.is_staff


