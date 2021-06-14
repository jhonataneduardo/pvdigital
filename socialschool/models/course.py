from django.db import models
from socialschool.models.group import Group
from socialschool.models.teacher import Teacher


class CourseCategory(models.Model):
    name = models.CharField(
        max_length=80
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        self.name


class Course(models.Model):
    name = models.CharField(
        max_length=120
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        CourseCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    vacancies = models.IntegerField(
        blank=True,
        null=True
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.RESTRICT,
        related_name='courses',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
