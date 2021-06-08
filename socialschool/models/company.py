from django.db import models
from django.db.models import fields


class Company(models.Model):
    CORPORATE_FUNCION_CHOICES = [
        ('primary', 'Primary'),
        ('secundary', 'Secundary'),
    ]

    parent_company = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    corporate_function = models.CharField(
        max_length=9,
        choices=CORPORATE_FUNCION_CHOICES,
        default='primary'
    )
    corporate_name = models.CharField(
        max_length=120
    )
    fantasy_name = fields.CharField(
        max_length=120
    )
    cnpj = models.CharField(
        max_length=14,
        verbose_name='CNPJ',
        unique=True
    )
    im = fields.CharField(
        max_length=11,
        verbose_name='Inscrição Municipal',
        unique=True
    )
    photo = models.ImageField(
        upload_to='companies/%Y/%m/%d/',
        blank=True)

    def __str__(self):
        return self.fantasy_name
