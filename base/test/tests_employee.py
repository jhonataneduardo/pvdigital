from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from base.models import company

from base.models.andress import Andress
from base.models.company import Company
from base.models.person import Person
from base.models.employee import Employee


class EmployeeCreateTest:
    def setUp(self):
        self.andress = Andress.objects.create(
            type="residential",
            street="Street TestCase",
        )
        self.company = Company.objects.create(
            corporate_name="TestCase",
            fantasy_name="TestCase",
            cnpj="12345612245612"
        )
        self.person = Person.objects.create(
            first_name='First Name TestCase',
            last_name='Last Name TestCase',
            date_of_birth='1991-07-13',
            gender='m',
            cpf='55441427000',
            andress=self.andress
        )
        self.employee = Employee.objects.create(
            person=self.person,
            company=self.company,
            type='employee'
        )


class EmployeeTestCase(EmployeeCreateTest, APITestCase):
    def test_POST_employee(self):
        """ Test API POST Employee"""
        url = reverse('list_create_employee')
        data = {
            'person': {
                'first_name': 'First Name TestCase',
                'last_name': 'Last Name TestCase',
                'date_of_birth': '1991-07-13',
                'gender': 'm',
                'cpf': '22047365031',
                'andress': {
                    'type': 'residential',
                    'zip_code': '81230162',
                    'street': 'Street TestCase',
                    'number': '123',
                    'complement': 'TestCase complement',
                    'district': 'TestCase distric',
                    'city': 'TestCase city',
                    'state': 'TestCase state',
                    'country': 'TestCase country'
                },
            },
            'company': self.company.id,
            'type': 'employee'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, response.content.decode('utf8'))

    def test_LIST_employee(self):
        url = reverse('list_create_employee')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.content.decode('utf8'))

    def test_GET_employee(self):
        url = reverse('get_update_delete_employee', args=[self.employee.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.content.decode('utf8'))

    def test_UPDATE_employee(self):
        url = reverse('get_update_delete_employee', args=[self.employee.id])
        data = {
            'id': self.employee.id,
            'person': {
                'first_name': 'First Name TestCase 2',
                'last_name': 'Last Name TestCase 2',
                'date_of_birth': '1991-07-13',
                'gender': 'm',
                'cpf': '55441427000',
                'andress': {
                    'type': 'residential',
                    'zip_code': '81230162',
                    'street': 'Street TestCase',
                    'number': '123',
                    'complement': 'TestCase complement',
                    'district': 'TestCase distric',
                    'city': 'TestCase city',
                    'state': 'TestCase state',
                    'country': 'TestCase country'
                },
            },
            'company': self.company.id,
            'type': 'voluntary'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.content.decode('utf8'))

    def test_DETELE_empployee(self):
        """ Test API DELETE Employee """
        url = reverse('get_update_delete_employee', args=[self.employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
