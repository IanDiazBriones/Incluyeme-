from django.test import TestCase
from .models import *

class BusTest(TestCase):
    def create_bus(self, PATENTE="PK-FD-56", MARCA="Mercedez Benz", MODELO="Zong-Tong"):
        return Bus(Patente = PATENTE, Marca = MARCA, Modelo = MODELO)

    def test_bus(self):
        bus_test = self.create_bus()
        self.assertTrue(isinstance(bus_test, Bus))
        self.assertEqual(bus_test.__str__(),bus_test.Patente)

# Create your tests here.
