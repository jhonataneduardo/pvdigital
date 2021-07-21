from django.db import models


TYPE_CHOICES = [
    ('residential', 'Residential'),
    ('other', 'Other'),
]


class Andress(models.Model):
    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        default='residential',
        blank=True
    )
    zip_code = models.CharField(
        max_length=8,
        blank=True
    )
    street = models.CharField(
        max_length=80,
        blank=True
    )
    number = models.CharField(
        max_length=5,
        blank=True
    )
    complement = models.CharField(
        max_length=80,
        blank=True
    )
    district = models.CharField(
        max_length=80,
        blank=True
    )
    city = models.CharField(
        max_length=80,
        blank=True
    )
    state = models.CharField(
        max_length=80,
        blank=True
    )
    country = models.CharField(
        max_length=80,
        blank=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'({self.type}) {self.street}, {self.number}'
