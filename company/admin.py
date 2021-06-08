from django.contrib import admin
from company.models.company import Company


@admin.register(Company)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['fantasy_name', 'cnpj', 'corporate_function']
