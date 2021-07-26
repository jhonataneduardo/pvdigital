from django.db import models
from django.utils.translation import gettext as _
from base.models.person import Person


class Student(models.Model):
    person = models.OneToOneField(
        Person,
        verbose_name=_('Person'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.person.first_name

