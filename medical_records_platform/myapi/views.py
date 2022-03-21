from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from .serializers import RoleSerializer
from .models import User
from .models import Role
from .models import Measurements
from .models import History
from .models import Billing

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('user')
    serializer_class = RoleSerializer

class MeasurementsViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all().order_by('user')
    serializer_class = RoleSerializer
    
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all().order_by('user')
    serializer_class = RoleSerializer

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all().order_by('user')
    serializer_class = RoleSerializer