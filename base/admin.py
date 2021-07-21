from django.contrib import admin
from base.models.company import Company
from base.models.person import Person
from base.models.andress import Andress

admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Andress)
