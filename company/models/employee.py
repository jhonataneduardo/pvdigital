from django.db import models
from accounts.models.profile import Profile
from company.models.company import Company
from company.models.andress import Andress


class Employee(models.Model):
    LIST_TYPE = [
        ('employee', 'Employee'),
        ('voluntary', 'Voluntary')
    ]

    profile = models.OneToOneField(
        Profile,
        related_name='employee',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=120
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    cpf = models.CharField(
        max_length=11,
        unique=True
    )
    type = models.CharField(
        max_length=10,
        choices=LIST_TYPE,
        blank=True
    )
    andresses = models.ManyToManyField(
        Andress,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.profile.first_name
