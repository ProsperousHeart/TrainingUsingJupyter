from rest_framework import serializers


# create a new serializer class that inherits from the imported module
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    # this CharField has a lot of pre-defined validation
    name = serializers.CharField(max_length=10)
