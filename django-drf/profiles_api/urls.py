from django.contrib import admin
from django.urls import path, include
from profiles_api import APIView

urlpatterns = [
    path("hello-view/", APIView.HelloApiView.as_view()),#this is the url for our api view. we will create a new file called urls.py in our profiles_api app and we will define the url for our api view in that file. and then we will include that url in our main urls.py file.
    #what is the use of as_view() method? it is used to convert the class based view into a function based view. it is used to call the get method of the class based view when we hit the url. it is used to create an instance of the class based view and then call the get method of that instance.
    path('hello-view/<int:pk>/', APIView.HelloApiView.as_view()),
]