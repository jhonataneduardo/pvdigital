from rest_framework import serializers
from company.models.employee import Employee
from company.serializers.andress import AndressSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    andresses = AndressSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        employee = super(EmployeeSerializer, self).create(validated_data)
        return employee
