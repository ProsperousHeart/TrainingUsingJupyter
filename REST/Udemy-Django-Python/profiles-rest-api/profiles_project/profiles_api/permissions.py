# import the base permissions module from Django REST framework
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    # this is called every time we make a request to our API
    # the result determines whether the user has the permission
    # to make the request / perform the action
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        # allow users to be able to view any profile in the system
        # don't want to apply any permissions if user is simply
        # trying to view a profile
        # This is completed by checking the safe methods list
        # provided by the REST Django framework

        # HTTP safe methods are non-destructive - allows you to
        # retrieve data but not change/modify/delete any objects
        if request.method in permissions.SAFE_METHODS:
            return True

        # making change on own profile?
        return obj.id == request.user.id
