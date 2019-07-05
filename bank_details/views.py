from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Banks, Branches
import json
from django.http import HttpResponse
from django.db.models import Q
from bank_details.serializers import BranchesSerializer, BanksSerializer
from rest_framework.pagination import LimitOffsetPagination

class BankDetail(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BranchesSerializer
    def get_queryset(self, *args, **kwargs):
        ifsc = self.request.query_params.get('ifsc')
        branches = Branches.objects.filter(ifsc=ifsc)
        return branches


class BranchDetail(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BranchesSerializer
    def get_queryset(self, *args, **kwargs):
        name = self.request.query_params.get('name')
        city = self.request.query_params.get('city')
        bank = Banks.objects.get(name=name)
        criterion_one = Q(bank=bank)
        criterion_two = Q(city=city)
        branches = Branches.objects.filter(criterion_one & criterion_two)
        return branches
