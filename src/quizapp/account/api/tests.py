# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status
from django.contrib.auth.models import User


# Create your tests here.
class UserViewSetTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='mentor', password='password')

    def test_get_current_user(self):
        response = self.client.get(reverse('api:account:user-current'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.login(username=self.user.username, password='password')
        response = self.client.get(reverse('api:account:user-current'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)