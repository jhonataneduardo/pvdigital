from django.db import models
from django.utils.translation import gettext as _
from base.models.person import Person


class Teacher(models.Model):

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    about = models.TextField(
        verbose_name=_('About')
    )

    def __str__(self):
        return self.person.first_name