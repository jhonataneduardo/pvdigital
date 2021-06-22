from rest_framework import serializers
from company.models.andress import Andress


class AndressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Andress
        fields = '__all__'
