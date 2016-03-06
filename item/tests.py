from django.contrib.auth.models import User

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from .serializers import ItemSerializer
from item.models import Item
from .views import ItemViewSet

# Create your tests here.

class ItemTests(APITestCase):
    fixtures = ['initial_data']

    def test_read_item(self):
        """
        Ensure we can read item object.

        """
        url = reverse("item-detail", kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Item.objects.count(), 2)

    def test_create_item(self):
        """
        Ensure we can create a new item object.

        """
        url = reverse("item-list")
        data = {"item_name": "joy","item_price": 100, "item_description": "ttttttttttttttt"}
        request = self.client.post(url, data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.last().item_name, 'joy')
        self.assertEqual(Item.objects.count(), 3)

    def test_update_item(self):
        """
        Ensure we can update item object.

        """
        url = reverse("item-detail", kwargs={'pk': Item.objects.first().pk})
        data = {"item_name": "new_item1","item_price": 200, "item_description": "new_item1"}
        request = self.client.put(url, data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        """
        Ensure we can delete item object.

        """
        url = reverse("item-detail", kwargs={'pk': Item.objects.last().pk})
        request = self.client.delete(url, format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
