from rest_framework import serializers
from school.models.teacher import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'