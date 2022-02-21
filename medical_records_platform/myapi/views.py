from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from .serializers import RoleSerializer
from .models import User
from .models import Role

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('user')
    serializer_class = RoleSerializer
