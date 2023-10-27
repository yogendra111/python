from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register('companies', CompanyViewSet)
router.register("employees", EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
