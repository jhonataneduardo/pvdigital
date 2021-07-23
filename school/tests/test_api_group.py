from django.urls import reverse
from django.test.testcases import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from school.models.teacher import Teacher


class GroupCreateTest:
    pass


class GroupTestCase(GroupCreateTest, TestCase):
    def test_POST_group(self):
        """ Test API POST Group"""
        url = reverse('list_create_group')
        data = {
            'teacher': self.teacher.id,
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
            'teacher': self.teacher.id,
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
