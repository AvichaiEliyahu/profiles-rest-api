from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Returns a list of API View features"""
        an_apiview = [
            'feature 1',
            'feature 2',
            'feature 3',
            'feature 4',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
