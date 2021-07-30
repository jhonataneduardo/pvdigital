from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from school.models.teacher import Teacher
from school.models.student import Student
from school.models.group import Group
from school.models.course import Course
from school.models.enrollment import Enrollment

from base.models.andress import Andress
from base.models.company import Company
from base.models.person import Person

import json


class EnrollmentCreateTest:
    def setUp(self):
        self.andress = Andress.objects.create(
            type='residential',
            zip_code='81230162',
            street='Street TestCase',
            number='123',
            complement='TestCase complement',
            district='TestCase distric',
            city='TestCase city',
            state='TestCase state',
            country='TestCase country'
        )
        self.company = Company.objects.create(
            corporate_name="TestCase",
            fantasy_name="TestCase",
            cnpj="34090032000147"
        )
        self.person = Person.objects.create(
            first_name="First Name TestCase",
            last_name="Last Name TestCase",
            date_of_birth="1991-07-13",
            gender="m",
            cpf="36816119045",
            andress=self.andress
        )
        self.teacher = Teacher.objects.create(
            person=self.person,
            about="TestCase about"
        )
        self.group = Group.objects.create(
            name="TestCase name",
            teacher=self.teacher,
            description="TestCase description"
        )
        self.course = Course.objects.create(
            name='TestCase name',
            group=self.group,
            teacher=self.teacher
        )
        self.student = Student.objects.create(
            person=self.person
        )
        self.enrollment = Enrollment.objects.create(
            number='123',
            student=self.student,
            state='draft'
        )
        self.enrollment.courses.set([self.course.id])
        self.enrollment.save()


class EnrollmentTestCase(EnrollmentCreateTest, APITestCase):
    def test_POST_enrollment(self):
        """ Test API POST Enrollment"""
        url = reverse('list_create_enrollment')
        data = {
            'number': '1234',
            'student': self.student.id,
            'courses': [self.course.id],
            'state': 'draft'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, response.content.decode('utf8'))

    def test_LIST_enrollment(self):
        """ Test API LIST Enrollment"""
        url = reverse('list_create_enrollment')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GET_enrollment(self):
        """ Test API GET Enrollment"""
        url = reverse('get_update_delete_enrollment',
                      args=[self.enrollment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UPDATE_enrollment(self):
        """ Test API UPDATE Enrollment"""
        url = reverse('get_update_delete_enrollment',
                      args=[self.enrollment.id])
        data = {
            'id': self.course.id,
            'number': '1234',
            'student': self.student.id,
            'courses': [self.course.id],
            'state': 'reserved'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(json.loads(response.content.decode('utf8')), data)

    def test_DELETE_enrollment(self):
        """ Test API DELETE Enrollment"""
        url = reverse('get_update_delete_enrollment',
                      args=[self.enrollment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
