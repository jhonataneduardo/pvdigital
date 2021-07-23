from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class CompanyTestCase(APITestCase):

    def teste_POST_company(self):
        url = reverse('list_create_company')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_LIST_company(self):
        url = reverse('list_create_company')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)