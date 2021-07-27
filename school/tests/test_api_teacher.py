from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from base.models.andress import Andress
from base.models.company import Company
from base.models.person import Person
from school.models.teacher import Teacher

import json


class TeacherCreateTest:
    def setUp(self):
        self.andress = Andress.objects.create(
            type="residential",
            street="Street TestCase",
        )
        self.company = Company.objects.create(
            corporate_name="TestCase",
            fantasy_name="TestCase",
            cnpj="12345612345612"
        )
        self.person1 = Person.objects.create(
            first_name="First Name TestCase",
            last_name="Last Name TestCase",
            date_of_birth="1991-07-13",
            gender="m",
            type="voluntary",
            cpf="123456",
            andress=self.andress,
            company=self.company
        )
        self.person2 = Person.objects.create(
            first_name="First Name TestCase",
            last_name="Last Name TestCase",
            date_of_birth="1991-07-13",
            gender="m",
            type="voluntary",
            cpf="78910",
            andress=self.andress,
            company=self.company
        )
        self.teacher1 = Teacher.objects.create(
            person=self.person1,
            about="TestCase about"
        )


class TeacherTestCase(TeacherCreateTest, APITestCase):
    def test_teacher_post(self):
        """ Test API POST Teacher """
        url = reverse('list_create_teacher')
        data = {
            'person': {
                'first_name': 'First Name TestCase',
                'last_name': 'Last Name TestCase',
                'date_of_birth': '1991-07-13',
                'gender': "m",
                'type': "voluntary",
                'cpf': "585858",
                'andress': {
                    'type': 'residential',
                    'street': 'Street TestCase',
                },
                'company': self.company.id
            },
            'about': 'TestCase about'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED, response.content)

    def test_teacher_list(self):
        url = reverse('list_create_teacher')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacher_get(self):
        url = reverse('get_update_delete_teacher', args=[self.teacher1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacher_update(self):
        url = reverse('get_update_delete_teacher', args=[self.teacher1.id])
        data = {
            'id': self.teacher1.id,
            'person': {
                'first_name': 'First Name TestCase 2',
                'last_name': 'Last Name TestCase 2',
                'date_of_birth': '1991-07-13',
                'gender': "m",
                'type': "voluntary",
                'cpf': "58585885",
                'andress': {
                    'type': 'residential',
                    'street': 'Street TestCase 2',
                },
                'company': self.company.id
            },
            'about': "TestCase Update 2"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacher_delete(self):
        """ Test API DELETE Teacher """
        url = reverse('get_update_delete_teacher', args=[self.teacher1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
