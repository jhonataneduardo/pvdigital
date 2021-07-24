from django.db import models
from django.utils.translation import gettext as _
from school.models.group import Group
from school.models.teacher import Teacher


class Course(models.Model):
    name = models.CharField(
        verbose_name=_('Course name'),
        max_length=120
    )
    group = models.ForeignKey(
        Group,
        verbose_name=_('Group'),
        on_delete=models.SET_NULL,
        related_name='courses',
        null=True
    )
    teacher = models.ForeignKey(
        Teacher,
        verbose_name=_('Teacher'),
        on_delete=models.SET_NULL,
        related_name='courses',
        null=True
    )

    def __str__(self):
        return self.name
