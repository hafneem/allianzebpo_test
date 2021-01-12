import random

from decimal import Decimal
from datetime import datetime

from rest_framework import serializers
from django.utils import timezone
from api.models import Branches


class BankDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = '__all__'


class FilteredBranchesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = '__all__'
