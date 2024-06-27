from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product

class InventoryApiTests(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(product_id=1, product_name='Test Product 1', description='Description 1', price=10.0)
        self.product2 = Product.objects.create(product_id=2, product_name='Test Product 2', description='Description 2', price=20.0)
        
        self.client = APIClient()

    def test_inventory_json(self):
        response = self.client.get('/api/v1/inventory/json/')
        self.assertEqual(response.status_code, 200)
        products = response.json()
        self.assertEqual(len(products), 2)

    def test_inventory_rest(self):

        response = self.client.get('/api/v1/inventory/rest/')
        self.assertEqual(response.status_code, 200)
        products = response.json()
        self.assertEqual(len(products), 2)

    def test_inventory_xml(self):

        response = self.client.get('/api/v1/inventory/xml/')
        self.assertEqual(response.status_code, 200)

        self.assertIn('<products>', response.content.decode('utf-8'))
        self.assertIn('<product_id>', response.content.decode('utf-8'))

