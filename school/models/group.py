from django.db import models
from django.utils.translation import gettext as _
from school.models.teacher import Teacher


class Group(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=80,
        blank=True
    )
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
        return self.name