from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # list of all objects when we create a new one
    serializer_class = UserSerializer # tells the view what data we need to accept
    permission_classes = [AllowAny] # specifies who can use this
