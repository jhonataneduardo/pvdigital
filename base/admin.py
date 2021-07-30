from django.contrib import admin
from base.models.company import Company
from base.models.person import Person
from base.models.andress import Andress
from base.models.employee import Employee

admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Andress)
admin.site.register(Employee)
