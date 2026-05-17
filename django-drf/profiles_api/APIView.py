from restframework.views import APIView
from restframework.response import Response

class HelloApiView(APIView):

    def get(self,request ,format=None):
        an_apiview=[
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to urls'    
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})