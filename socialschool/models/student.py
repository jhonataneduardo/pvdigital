from django.db import models


class Student(models.Model):
    photo = models.ImageField(
        upload_to='student/%Y/%m/%d/',
        blank=True
    )
    first_name = models.CharField(
        max_length=80
    )
    last_name = models.CharField(
        max_length=120
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=20,
        choices=[('m', 'Male'), ('f', 'Female')]
    )
    active = models.BooleanField(
        default=True
    )
    description = models.TextField()

    def __str__(self):
        return self.first_name
