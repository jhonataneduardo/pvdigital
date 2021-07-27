from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models.teacher import Teacher
from school.models.group import Group
from school.models.student import Student

from base.models.andress import Andress
from base.models.company import Company
from base.models.person import Person

import json


class StudentCreateTest:
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
            cpf="123455558",
            andress=self.andress,
            company=self.company
        )
        self.person2 = Person.objects.create(
            first_name="First Name TestCase",
            last_name="Last Name TestCase",
            date_of_birth="1991-07-13",
            gender="m",
            type="voluntary",
            cpf="1234533",
            andress=self.andress,
            company=self.company
        )
        self.teacher = Teacher.objects.create(
            person=self.person1,
            about="TestCase about"
        )
        self.group = Group.objects.create(
            teacher=self.teacher,
            description="TestCase description"
        )
        self.student = Student.objects.create(person=self.person1)


class StudentTestCase(StudentCreateTest, APITestCase):
    def test_POST_student(self):
        """ Test API POST Student"""
        url = reverse('list_create_student')
        data = {
            'person': {
                'first_name': 'First Name TestCase',
                'last_name': 'Last Name TestCase',
                'date_of_birth': '1991-07-13',
                'gender': 'm',
                'type': 'voluntary',
                'cpf': '1234958',
                'andress': {
                    'type': 'residential',
                    'street': 'Street TestCase',
            },
            'company': self.company.id
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_LIST_student(self):
        """ Test API LIST Student"""
        url = reverse('list_create_student')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GET_student(self):
        """ Test API GET Student"""
        url = reverse('get_update_delete_student', args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UPDATE_student(self):
        """ Test API UPDATE Student"""
        url = reverse('get_update_delete_student', args=[self.student.id])
        data = {
            'person': {
                'first_name': 'First Name TestCase 2',
                'last_name': 'Last Name TestCase 2',
                'date_of_birth': '1991-07-13',
                'gender': 'm',
                'type': 'voluntary',
                'cpf': '1234951',
                'andress': {
                    'type': 'residential',
                    'street': 'Street TestCase 2',
            },
            'company': self.company.id
            }
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_DELETE_student(self):
        """ Test API DELETE Student"""
        url = reverse('get_update_delete_student', args=[self.student.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
