from rest_framework import serializers
from base.models.andress import Andress


class AndressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Andress
        fields = '__all__'
