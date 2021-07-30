from django.db import models
from django.utils.translation import gettext as _

from base.models.person import Person
from base.models.company import Company


LIST_TYPE = [
    ('employee', _('Employee')),
    ('voluntary', _('Voluntary')),
    ('teacher', _('Teacher')),
    ('student', _('Student')),
]


class Employee(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True
    )
    type = models.CharField(
        max_length=10,
        choices=LIST_TYPE,
        blank=True
    )

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name}'
