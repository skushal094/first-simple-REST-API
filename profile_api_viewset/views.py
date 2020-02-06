from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from profile_api_apiview import serializers


# Create your views here.
class HelloViewSet(viewsets.ViewSet):
    """Simple ViewSet API"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Handles GET requests"""
        a_message = {
            'message': 'Hello',
            'another message': 'this is list method to handle GET requests'
        }
        return Response(a_message)

    def create(self, request):
        """Handles POST requests"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data.get('name')
            return Response({'name': f'{data}'})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):
        """Handles PUT method"""
        return Response({'HTTP_METHOD': request.method})

    def retrieve(self, request, pk=None):
        """Handles GET requests with specific ID"""
        return Response({'HTTP_METHOD': request.method})

    def partial_update(self, request, pk=None):
        """Handles PATCH method"""
        return Response({'HTTP_METHOD': request.method})

    def destroy(self, request, pk=None):
        """Handles DELETE requests"""
        return Response({'HTTP_METHOD': request.method})
