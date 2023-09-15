from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_staff)


class IsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsSuperUserOrOwnerOrReadOnly(BasePermission):
    def has__object_permission(self, request, view, obj):
        if request.method == 'POST':
            return (request.user.is_authenticated)
        return (obj.author == request.user or request.user.is_staff)
