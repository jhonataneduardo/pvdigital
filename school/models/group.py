from django.db import models
from django.utils.translation import gettext as _
from school.models.teacher import Teacher


class Group(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        verbose_name=_('Teacher'),
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField(
        verbose_name=_('Description')
    )

    def __str__(self):
        return self.teacher.person.first_name