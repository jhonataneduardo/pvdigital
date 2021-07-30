from rest_framework import serializers

from base.models.employee import Employee
from base.models.andress import Andress
from base.models.person import Person

from base.serializers.person import PersonSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def update(self, instance, validated_data):
        person = validated_data.pop('person', None)
        andress = person.pop('andress', None)

        # update andress
        if instance.person.andress:
            obj_andress = Andress.objects.get(pk=instance.person.andress.id)
            for key, value in andress.items():
                setattr(obj_andress, key, value)
            obj_andress.save()
        else:
            obj_andress = Andress.objects.create(**andress)

        # update person
        obj_person = Person.objects.get(pk=instance.person.id)
        for key, value in person.items():
            setattr(obj_person, key, value)
        obj_person.andress = obj_andress
        obj_person.save()

        instance.person = obj_person

        # update employee
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

    def create(self, validated_data):
        person = validated_data.pop('person', None)
        andress = person.pop('andress', None)

        if andress:
            andress = Andress.objects.create(**andress)

        if person:
            person['andress'] = andress
            person = Person.objects.create(**person)

        instance = Employee.objects.create(**validated_data, person=person)

        return instance
