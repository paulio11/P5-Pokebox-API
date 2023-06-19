from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission class that grants full access to owners,
    and read-only access to others.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission class that grants full access to admin users,
    and read-only access to others.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_staff
