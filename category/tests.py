from django.test import TestCase

from rest_framework import APITestCase
from rest_framework import APIRequestFactory
from rest_framework import reverse
from rest_framework import status

from .serializers import CategorySerializer
from .models import Category

# Create your tests here.

class CategoryTest(APITestCase):
    pass
