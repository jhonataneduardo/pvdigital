from django.db import models


class Andress(models.Model):
    LIST_TYPE = [
        ('residential', 'Residential'),
        ('other', 'Other'),
    ]

    type = models.CharField(
        max_length=12,
        choices=LIST_TYPE,
        default='residential'
    )
    zip_code = models.CharField(
        max_length=8
    )
    street = models.CharField(
        max_length=80
    )
    number = models.IntegerField()
    complement = models.CharField(
        max_length=80
    )
    district = models.CharField(
        max_length=80
    )
    city = models.CharField(
        max_length=80
    )
    state = models.CharField(
        max_length=80
    )
    country = models.CharField(
        max_length=80
    )

    def __str__(self):
        return f'{self.street}, {self.number}'
