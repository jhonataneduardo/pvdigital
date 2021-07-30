from rest_framework import serializers
from school.models.enrollment import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enrollment
        fields = '__all__'