from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Simple serializer that take character input"""
    name = serializers.CharField(max_length=10)