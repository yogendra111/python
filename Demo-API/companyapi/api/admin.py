from django.contrib import admin
from .models import Employee, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
