from django.db import models
from django.utils.translation import gettext as _
from base.models.person import Person
from school.models.course import Course


class Student(models.Model):
    person = models.OneToOneField(
        Person,
        verbose_name=_('Person'),
        on_delete=models.CASCADE
    )
    courses = models.ManyToManyField(
        Course,
        verbose_name=_('Courses')
    )

    def __str__(self):
        return self.person.first_name

