from django.db import models
from company.models.employee import Employee
from company.models.company import Company


class Teacher(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE
    )
    description = models.TextField()

    def __str__(self):
        return self.employee.profile.first_name
