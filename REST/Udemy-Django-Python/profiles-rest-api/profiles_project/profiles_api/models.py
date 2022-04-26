from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile in our system."""
    # provide various fields for models
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # custom model manager needed for user model so Django
    # knows how to create users & control using the Django CLI
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user's full name."""

        return self.name

    def get_short_name(self):
        """Used to get a user's short name."""

        return self.name

    # recommended for all Django models
    def __str__(self):
        """Django uses this when it needs to convert an object to a string.

        Returns string representation of our user."""

        return self.email
