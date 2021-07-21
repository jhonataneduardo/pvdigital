from django.db import models


CORPORATE_FUNCION_CHOICES = [
    ('primary', 'Primary'),
    ('secundary', 'Secundary'),
]


class Company(models.Model):
    parent_company = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    corporate_function = models.CharField(
        max_length=9,
        choices=CORPORATE_FUNCION_CHOICES,
        blank=True
    )
    corporate_name = models.CharField(
        max_length=120
    )
    fantasy_name = models.CharField(
        max_length=120
    )
    photo = models.ImageField(
        upload_to='companies/%Y/%m/%d/',
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
    cnpj = models.CharField(
        max_length=14,
        verbose_name='CNPJ'
    )
    im = models.CharField(
        max_length=11,
        verbose_name='Inscrição Municipal',
        unique=True,
        blank=True
    )

    def __str__(self):
        return self.fantasy_name
