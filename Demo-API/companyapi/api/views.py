from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer


# Create your views here.
# Company View
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    # /companies/id/employees
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emp, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                "error": "Company not exists"
            })


# Employee view
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
