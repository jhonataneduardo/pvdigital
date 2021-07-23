from django.http import response
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
            "type": "voluntary",
            "cpf": "7878",
            "andress": {
                "type": "residential",
                "street": "Street TestCase",
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_person(self):
        """ Test LIST Person """
        url = reverse('list_create_person')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
