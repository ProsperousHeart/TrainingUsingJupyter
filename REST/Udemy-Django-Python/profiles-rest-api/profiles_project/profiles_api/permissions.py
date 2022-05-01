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

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to udpate their own status."""

    # add "has object permission" just like with UpdateOwnProfile
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status."""

        # because this is only to allow users to udpate their own status,
        # we will allow all methods in SAFE METHODS through
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if user IS trying to update a status (not in SAFE METHOD)
        # need to make sure they own the status, or the user profile
        # assigned to the status is associated with the authenticated user
        return obj.user_profile_id == request.user.id
