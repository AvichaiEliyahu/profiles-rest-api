from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns a list of API View features"""
        an_apiview = [
            'feature 1',
            'feature 2',
            'feature 3',
            'feature 4',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})

    def post(self, request):
        """creat a hello message with our name"""

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk = None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk = None):
        """Handle object deletion"""
        return Response({'method' : "DELETE" })


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'feature1',
            'feature2',
            'feature3',
            'feature4',
        ]

        return Response({'message' : 'hello' , 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name  = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retreive(self, request, pk = None):
        """Handle getting an object by its id"""
        return Response({'http_method' : 'GET'})

    def update(self, request, pk = None):
        """Handle updating an object"""
        return Response({'http_method' : 'PUT'})

    def partial_update(self, reuqest, pk = None):
        """Handle updating part of an object"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk = None):
        """Handle removing an object"""
        return Response({'http_method' : 'DELETE'})
