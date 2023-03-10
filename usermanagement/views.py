from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import Users

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()