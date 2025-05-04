from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        # allow read only for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # allow write method for user is author and admin
        return obj.author == request.user or request.user.is_staff