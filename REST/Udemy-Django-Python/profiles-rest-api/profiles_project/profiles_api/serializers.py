from rest_framework import serializers

from profiles_api import models


# create a new serializer class that inherits from the imported module
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    # this CharField has a lot of pre-defined validation
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    # create a meta class that tells Django REST framework
    # what fields we want to take from our model
    class Meta:
        # assign model we want it to point to (our user profile model)
        model = models.UserProfile

        # what fields to use in the serializer
        fields = ('id', 'email', 'name', 'password')

        # define extra keyword arguments for your model
        # allows you to tell Django REST framework special attributes
        # you want to apply to those fields above
        # keys in teh dictionary are the fields you want to add custom args to
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}  # style for browsable API
            }
        }

    # create a special function that overwrites the CREATE functionality
    # this will allow us control over how users are created
    # we want to encrypt the PW as a hash
    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        # user.set_password(validated_data['password'])
        # user.save()

        return user

    # added to avoid clear text issue
    # https://github.com/LondonAppDev/profiles-rest-api/blob/master/profiles_api/serializers.py#L34
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)  # saves as hash

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items."""

    # set model serializer to ProfileFeedItem class in models.py
    class Meta:
        model = models.ProfileFeedItem

        # create fields based on the model
        # Django always has an INT "id" & automatically RO
        # since "created_on" is also autmatically created, it is RO
        fields = ('id', 'user_profile', 'status_text', 'created_on')

        # make user_profile the authenticated user
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }
