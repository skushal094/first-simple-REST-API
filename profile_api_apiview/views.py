from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status


# Create your views here.
class ProfileApiView(APIView):
    """APIView for simple model Profile"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Handles GET request on this APIView"""
        an_msg_list = [
            'Shah',
            'Kushal',
            'Python'
        ]
        return Response({'message': an_msg_list})

    def post(self, request):
        """Handles POST request and pass name to the serializer"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': 'Hello {}'.format(name)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles PUT requests (Updating)"""
        return Response({'message': 'PUT request'})

    def patch(self, request, pk=None):
        """Handles PATCH request (Partial Updating)"""
        return Response({'message': 'PATCH request'})

    def delete(self, request, pk=None):
        """Handles DELETE request (Deletion)"""
        return Response({'message': 'DELETE request'})
