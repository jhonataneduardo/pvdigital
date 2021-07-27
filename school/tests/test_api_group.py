from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from school.models.teacher import Teacher
from school.models.group import Group
from base.models.andress import Andress
from base.models.company import Company
from base.models.person import Person

import json


class GroupCreateTest:
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
        self.person1 = Person.objects.create(
            first_name="First Name TestCase",
            last_name="Last Name TestCase",
            date_of_birth="1991-07-13",
            gender="m",
            type="voluntary",
            cpf="1234568",
            andress=self.andress,
            company=self.company
        )
        self.person2 = Person.objects.create(
            first_name="First Name TestCase",
            last_name="Last Name TestCase",
            date_of_birth="1991-07-13",
            gender="m",
            type="voluntary",
            cpf="789108",
            andress=self.andress,
            company=self.company
        )
        self.teacher1 = Teacher.objects.create(
            person=self.person1,
            about="TestCase about"
        )
        self.teacher2 = Teacher.objects.create(
            person=self.person2,
            about="TestCase about"
        )
        self.group = Group.objects.create(
            name="TestCase name",
            teacher=self.teacher1,
            description="TestCase description"
        )


class GroupTestCase(GroupCreateTest, APITestCase):
    def test_POST_group(self):
        """ Test API POST Group"""
        url = reverse('list_create_group')
        data = {
            'name': 'TestCase name',
            'teacher': self.teacher2.id,
            'description': 'TestCase description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_LIST_group(self):
        """ Test API LIST Group"""
        url = reverse('list_create_group')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GET_group(self):
        """ Test API GET Group"""
        url = reverse('get_update_delete_group', args=[self.group.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UPDATE_group(self):
        """ Test API UPDATE Group"""
        url = reverse('get_update_delete_group', args=[self.group.id])
        data = {
            'id': self.group.id,
            'name': 'TestCase name 2',
            'teacher': self.teacher1.id,
            'description': 'TestCase description'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content.decode('utf8')), data)

    def test_DELETE_group(self):
        """ Test API DELETE Group"""
        url = reverse('get_update_delete_group', args=[self.group.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
