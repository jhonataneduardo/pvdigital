from django.db.models import fields
from rest_framework import serializers
from school.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'