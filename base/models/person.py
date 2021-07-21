from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from base.models.company import Company
from base.models.andress import Andress

User = get_user_model()

LIST_TYPE = [
    ('employee', _('Employee')),
    ('voluntary', _('Voluntary')),
    ('teacher', _('Teacher')),
    ('student', _('Student')),  
]

class Person(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='person'
    )
    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=60,
        blank=True
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=80,
        blank=True
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date of Birth"),
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=20,
        choices=[('m', _("Male")), ('f', _("Female"))],
        default="m"
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    type = models.CharField(
        max_length=10,
        choices=LIST_TYPE,
        blank=True
    )
    photo = models.ImageField(
        verbose_name=_("Photo"),
        upload_to='users/%Y/%m/%d/',
        blank=True,
        null=True
    )
    andress = models.ForeignKey(
        Andress,
        verbose_name=_("Andress"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )

    # docs br
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
        unique=True,
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"