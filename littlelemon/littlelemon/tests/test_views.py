from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title="Menu Item 1", price=12.00, inventory=100)
        Menu.objects.create(title="Menu Item 2", price=10.00, inventory=100)

        # Initialize the APIClient for making requests
        self.client = APIClient()

    def test_getall(self):
        # Get the URL for your view (replace 'menu-list' with your actual URL)
        url = reverse('menu')

        # Make a GET request to the view
        response = self.client.get(url)

        # Retrieve all Menu objects from the database
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)  # Serialize the data

        # Assert that the response status code is 200 (OK)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the serialized data matches the response data
        # self.assertEqual(response.data, serializer.data)
