from django.db import models
from socialschool.models.teacher import Teacher


class GroupConfig(models.Model):
    LIST_PERIODS = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('fulltime', 'Fulltime'),
    ]
    LIST_TYPE_VACANCIES = [
        ('by_group', 'By Group'),
        ('by_course', 'By Course'),
        ('unlimited', 'Unlimited')
    ]

    periods = models.CharField(
        max_length=10,
        choices=LIST_PERIODS,
        blank=True
    )
    type_vacancies = models.CharField(
        max_length=10,
        choices=LIST_TYPE_VACANCIES,
        blank=True
    )


class Group(models.Model):
    name = models.CharField(
        max_length=80
    )
    parent_group = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = models.TextField()
    group_config = models.ForeignKey(
        GroupConfig,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
