from django.db import models
from django.utils.translation import gettext as _

from school.models import Student
from school.models import Course


STATE_ENROLLMENT = [
    ('draft', _('Draft')),
    ('reserved', _('Reserved')),
    ('cancel', _('Cancel')),
    ('done', _('Done'))
]

class Enrollment(models.Model):
    number = models.CharField(
        verbose_name=_('Number'),
        max_length=9
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments',
        verbose_name=_('Student')
    )
    courses = models.ManyToManyField(
        Course,
        verbose_name=_('Courses')
    )
    state = models.CharField(
        verbose_name=_('State'),
        choices=STATE_ENROLLMENT,
        max_length=8
    )
