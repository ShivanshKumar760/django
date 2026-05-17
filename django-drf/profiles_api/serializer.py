from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class DemoSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    id= serializers.IntegerField()
    name = serializers.CharField(max_length=10)
    task = serializers.CharField(max_length=10)