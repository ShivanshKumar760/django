from rest_framework import serializers
from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class DemoSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    id= serializers.IntegerField()
    name = serializers.CharField(max_length=10)
    task = serializers.CharField(max_length=10)


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
         model=models.UserPorfile
         fields=('id','email','name','password')
         extra_kwargs={
             'password':{
                 'write_only':True,
                 'style':{'intput_type':'password'}
            }
        }
    
    def create(self,validated_data):
        user = models.UserPorfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

