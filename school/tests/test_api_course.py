from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from school.models.teacher import Teacher
from school.models.group import Group
from school.models.course import Course
from base.models.andress import Andress
from base.models.company import Company
from base.models.person import Person

import json


class CourseCreateTest:
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
            first_name="First Name TestCase",
            last_name="Last Name TestCase",
            date_of_birth="1991-07-13",
            gender="m",
            type="voluntary",
            cpf="1234568",
            andress=self.andress,
            company=self.company
        )
        self.teacher = Teacher.objects.create(
            person=self.person,
            about="TestCase about"
        )
        self.group = Group.objects.create(
            teacher=self.teacher,
            description="TestCase description"
        )
        self.course = Course.objects.create(
            name='TestCase name',
            group=self.group,
            teacher=self.teacher
        )


class CourseTestCase(CourseCreateTest, APITestCase):
    def test_POST_course(self):
        """ Test API POST Course"""
        url = reverse('list_create_course')
        data = {
            'name': 'TestCase name',
            'group': self.group.id,
            'teacher': self.teacher.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_LIST_course(self):
        """ Test API LIST Course"""
        url = reverse('list_create_course')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GET_course(self):
        """ Test API GET Course"""
        url = reverse('get_update_delete_course', args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UPDATE_course(self):
        """ Test API UPDATE Course"""
        url = reverse('get_update_delete_course', args=[self.course.id])
        data = {
            'id': self.course.id,
            'name': 'TestCase name update',
            'group': self.group.id,
            'teacher': self.teacher.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content.decode('utf8')), data)

    def test_DELETE_course(self):
        """ Test API DELETE Course"""
        url = reverse('get_update_delete_course', args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
