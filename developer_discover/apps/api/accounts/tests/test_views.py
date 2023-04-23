from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


class AccountViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_valid_data(self):
        valid_data = {"username": "test1", "password": "test-password", "name": "test"}
        response = self.client.post(reverse("sign-up"), valid_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_exist_user_data(self):
        invalid_data = {"username": "", "password": "test-password", "name": "test"}
        response = self.client.post(reverse("sign-up"), invalid_data, format="json")
        self.assertEqual(response.status_code, 400)
