from django.contrib import admin
from company.models.company import Company
from company.models.employee import Employee
from company.models.andress import Andress


@admin.register(Company)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['fantasy_name', 'cnpj', 'corporate_function']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'type']


@admin.register(Andress)
class AndressAdmin(admin.ModelAdmin):
    list_display = ['street', 'number', 'district', 'state', 'country', 'type']
