from rest_framework import serializers
from bank_details.models import Banks, Branches

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = 'ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state'
        depth = 1

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fileds = 'id', 'name'
