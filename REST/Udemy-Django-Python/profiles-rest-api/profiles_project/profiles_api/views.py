# import APIView class from rest_framework.views module
from rest_framework.views import APIView
# import Response class from rest_framework.response module
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    # API Views works by defining functions that match standard HTTP methods.
    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        # return a Response instance
        #     Response({'message': '', 'variable': value, ...})
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        # create our serializer - pass in the request information
        # serializer = serializers.HelloSerializer(data=request.data)
        serializer = self.serializer_class(data=request.data)

        # check if serializer has valid data
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            # return a message about what went wrong and the status
            # 400 means bad request to API
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handles updating an object."""

        # for now return what this method does
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only update fields provided in the request."""

        # return a dictionary with what this method does
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        # return a dictionary with what this method does
        return Response({'method': 'delete'})
