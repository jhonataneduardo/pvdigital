import inspect
from rest_framework import serializers
from base.models.person import Person
from base.models.andress import Andress
from base.serializers.andress import AndressSerializer


class PersonSerializer(serializers.ModelSerializer):
    andress = AndressSerializer()

    class Meta:
        model = Person
        fields = '__all__'
        extra_kwargs = {
            'cpf': {
                'validators': [],
            }
        }

    def update(self, instance, validated_data):
        andress = validated_data.pop('andress', None)
        if andress:
            obj_andress = Andress.objects.get(pk=instance.andress.id)
            for key, value in andress.items():
                setattr(obj_andress, key, value)
            obj_andress.save()
            instance.andress = obj_andress
        return super(PersonSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        exist_cpf = Person.objects.filter(cpf=validated_data['cpf']).exists()
        if exist_cpf:
            raise serializers.ValidationError("Número de CPF já existe.")
            
        andress = validated_data.pop('andress', None)
        if andress:
            andress = Andress.objects.create(**andress)

        instance = Person.objects.create(**validated_data)
        instance.andress = andress
        instance.save()
        return instance
