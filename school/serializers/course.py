from django.db.models import fields
from rest_framework import serializers
from school.models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'