from rest_framework import serializers

from api.models import Branches


class BankDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = '__all__'


class FilteredBranchesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = '__all__'
