# import APIView class from rest_framework.views module
from rest_framework.views import APIView
# import Response class from rest_framework.response module
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View."""

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
