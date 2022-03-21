# serializers.py
from rest_framework import serializers

from .models import User
from .models import Role
from .models import Measurements
from .models import History
from .models import Billing


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

class MeasurementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = (
            'user',
            'height',
            'weight',
            'blood_pressure',
            'glucose',
            'cholesterol',
            'iron',
            'pulse',
            'blood_oxygen'
        )

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = (
            'user',
            'family_history',
            'medical_history',
            'medications'
        )

class BillingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = (
            'user',
            'billing_address',
            'insurance_address',
            'member_id',
            'group_num',
            'insurance_plan_name',
            'insurance_plan_type',
            'holder_name',
            'holder_relation',
            'credit_card_num'
        )