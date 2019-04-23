from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from .models import *


class CustomUserTest(TestCase): #Model Custom User Test
    def create_user(self, USERNAME = "Test", RUT = "20516849-9", EMAIL = "admin@test.com", NOMBRE = "Pepito", TELEFONO = "123456789"):
        return CustomUser(username = USERNAME, rut = RUT, email = EMAIL, nombre = NOMBRE, telefono = TELEFONO)

    def test_user_creation(self):
        model_test = self.create_user()
        self.assertTrue(isinstance(model_test, CustomUser))
        self.assertEqual(model_test.__str__(),model_test.email)
        self.assertFalse(model_test.es_admin)

    """"def register_view_test(self): # View Register Test
        model_test = self.create_user()
        url = reverse("")"""
# Create your tests here.
