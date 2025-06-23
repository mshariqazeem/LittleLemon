from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        MenuItem.objects.create(title="Burger", price=10, inventory=100)
        MenuItem.objects.create(title="Pizza", price=15, inventory=50)
        MenuItem.objects.create(title="Salad", price=8, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))

        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
