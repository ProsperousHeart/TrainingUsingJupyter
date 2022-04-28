from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# used to retrieve settings from settings.py file in project settings
from django.conf import settings

# create profile manager
class UserProfileManager(BaseUserManager):
    """Manager for user priofiles.
    Helps Django work with our custom user model."""

    # create user with model
    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        # logic to create a new user in the system

        if not email:
            raise ValueError('Users must have an email address.')

        # normalize the email address - convert to lower case
        email = self.normalize_email(email)

        # create a new user profile object
        user = self.model(email=email, name=name)

        # set password - this encrypts the PW for us
        # password is converted to a hash stored in the DB - no clear text
        # therefore a None value will not allow for the user to be created
        user.set_password(password)

        # save using same DB used when we created the UserProfileManager
        # Django can support multiple databases
        user.save(using=self._db)

        return user

    # create super user
    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True  # automatically created by PermissionsMixin
        user.is_staff = True

        user.save(using=self._db)

        return user


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

class ProfileFeedItem(models.Model):
    """Profiles status update."""

    # setting up a foreign key field it sets up a
    # FK relationship in the DB to a remote model
    # BENEFIT:  ensure integrity of the DB is maintained
    user_profile = models.ForeignKey(
        # 1st argument:  name of the model that is the remote model for the FK
        # don't want to hard code - use the settings.py file
        settings.AUTH_USER_MODEL,
        # 2nd argument:  on delete - tells DB what to do if remove field is deleted
        # if set to CASCADE, it cascades changes downt hrough related fields
        on_delete=models.CASCADE
    )

    # contains text of feed update
    status_text = models.CharField(max_length=255)

    # every time new created, automatically add date/time stamp
    created_on = models.DateTimeField(auto_now_add=True)

    # str representation of our model
    # (what to do when convert model instance to a STR)
    def __str__(self):
        """Return the model as a string."""
        return self._status_text
