from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profiles_api.serializer import HelloSerializer,DemoSerializer
from profiles_api import models
from profiles_api import serializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
#the TokenAuthentication system work by genrating random genrated string and when we made any request 
#to the api we send this token string also in the request to check its authenticated or not 
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class=serializer.UserProfileSerializers
    queryset=models.UserPorfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_bakend=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES