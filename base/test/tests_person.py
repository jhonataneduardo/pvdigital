from rest_framework.test import APITestCase
from base.models.person import Person
from django.urls import reverse
from rest_framework import status


class PersonTestCase(APITestCase):

    def test_POST_person(self):
        """ Test POST Person """
        url = reverse('list_create_person')
        data = {
            "first_name": "First Name TestCase",
            "last_name": "Last Name TestCase",
            "date_of_birth": "1991-07-13",
            "gender": "m",
            "cpf": "43806144095",
            "andress": {
                'type': 'residential',
                'zip_code': '81230162',
                'street': 'Street TestCase',
                'number': '123',
                'complement': 'TestCase complement',
                'district': 'TestCase distric',
                'city': 'TestCase city',
                'state': 'TestCase state',
                'country': 'TestCase country'
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, response.content.decode('utf8'))

    def test_list_person(self):
        """ Test LIST Person """
        url = reverse('list_create_person')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
