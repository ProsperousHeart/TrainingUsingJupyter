# import APIView class from rest_framework.views module
from rest_framework.views import APIView
# import Response class from rest_framework.response module
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
# import Token Authentication
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""
    serializer_class = serializers.HelloSerializer

    def list(self, request):  # typically a HTTP GET to the root of an endpoint
        """Return a hello message."""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    # CREATE - takes care of the HTTP POST function
    # creates new objects in the system
    def create(self, request):
        """Create a new hello message."""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # RETRIEVE - gets a specific object by it's ID
    def retrieve(self, request, pk=None):
        """Handles getting an object by it's ID."""

        return Response({'http_method': 'GET'})

    # UPDATE - corresponds to the HTTP PUT
    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    # PARTIAL_UPDATE - corresponds to HTTP PATCH method
    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    # DESTROY - corresponds to HTTP DELETE method
    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""
    # ModelViewSet is a special ViewSet by the Django REST framework
    # that takes care of all of the logic for CRU our model items

    # define the serializer class - this serializer has the model
    # in the metadata so it knows which model to look for
    # to handle user objects
    serializer_class = serializers.UserProfileSerializer

    # query the set which tells the ViewSet how to retrieve
    # the object from our DB
    queryset = models.UserProfile.objects.all() # this retrieves all of them

    # add an authentication class variable below the query set variable
    # ensure a comma is after it to ensure Python knows it's a tuple
    authentication_classes = (TokenAuthentication,)

    # define permission classes that will be applied
    permission_classes = (permissions.UpdateOwnProfile,)

    # filters to use
    filter_backends = (filters.SearchFilter,)

    #fields to filter by
    search_fields = ('name', 'email')
