from django.db import models
from rest_framework import serializers
from company.models.employee import Employee
from accounts.models.profile import Profile


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        employee = super(EmployeeSerializer, self).create(validated_data)
        return employee
