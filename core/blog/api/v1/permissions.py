from rest_framework import permissions


# only the user can update this post who is the owner of this post
class IsOwnerOrReadOnly(permissions.BasePermission):

    # review object permission
    def has_object_permission(self, request, view, obj):
        # permissions.SAFE_METHODS include only method=get (list and retrieve)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.user == request.user
