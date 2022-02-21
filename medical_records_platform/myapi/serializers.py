# serializers.py
from rest_framework import serializers

from .models import User
from .models import Role

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id'
            'first_name',
            'last_name',
            'address',
            'date_birth',
            'sex',
            'primary_care_provider'
        )

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = (
            'user',
            'role',
            'status',
            'time_status'
        )