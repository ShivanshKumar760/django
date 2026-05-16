from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin

# Create your models here.

class UserPorfile(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)#this field is used to determine if the user is a staff member or not. it is used to determine if the user has access to the django admin site or not.

    USERNAME_FIELD = 'email' #by default, if we set USERNAME_FIELD to email, then we will use email to authenticate the user instead of username. this is because we want to use email as the unique identifier for the user instead of username. if we set USERNAME_FIELD to username, then we will use username to authenticate the user instead of email. if we set USERNAME_FIELD to something else, then we will use that field to authenticate the user instead of email or username. in this case, we want to use email as the unique identifier for the user, so we set USERNAME_FIELD to email. and  its required by default
    REQUIRED_FIELDS = ['name']

    objects = UserProfileManager()#this is the manager for the user profile model. it is used to create a new user and a new superuser. it is also used to authenticate a user.

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):#what is this __str__ method? 
        #it is a special method in python that is used to return a 
        # string representation of an object. it is called when you use the print() 
        # function on an object or when you convert an object to a string using the 
        # str() function. in this case, it will return the email of 
        # the user profile when you print the user profile object.
        #demo 
        # class Person:
        #     def __init__(self, name):
        #         self.name = name
        #     def __str__(self):
        #         return self.name
        # person = Person("John")
        # print(person) # Output: John
        return self.email
