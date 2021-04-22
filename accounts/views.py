from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from .models import (
    Manager, Employee
)
from .serializers import (
    UserDetailSerializer, RegisterManagerSerializer, EmployeeSerializer
    )
from .utils import required_field_validator


import traceback
# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

class ManagerView(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user



class RegisterView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterManagerSerializer


class CreateEmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ListEmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination




