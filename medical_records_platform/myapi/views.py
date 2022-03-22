from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from .serializers import RoleSerializer
from .models import User
from .models import Role

from django.http import JsonResponse
from time import sleep

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('user')
    serializer_class = RoleSerializer

def index(request):
    json_payload = {
        "message": "Hello world!"
    }
    sleep(10)
    return JsonResponse(json_payload)
