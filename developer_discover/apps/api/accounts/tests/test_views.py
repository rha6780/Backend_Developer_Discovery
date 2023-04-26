from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


class UserSignUpViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.valid_data = {"email": "test1@test.com", "password": "test-password", "name": "test"}
        cls.invalid_email_data = {"email": "", "password": "test-password", "name": "test"}
        cls.invalid_password_data = {"email": "", "password": "test", "name": "test"}

    def test_valid_data(self):
        response = self.client.post(reverse("sign-up"), self.valid_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_exist_user_data(self):
        response = self.client.post(reverse("sign-up"), self.valid_data, format="json")
        self.assertEqual(response.status_code, 200)

        error_response = self.client.post(reverse("sign-up"), self.valid_data, format="json")
        self.assertEqual(error_response.status_code, 400)

    def test_invalid_email_data(self):
        response = self.client.post(reverse("sign-up"), self.invalid_email_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_invalid_password_data(self):
        response = self.client.post(reverse("sign-up"), self.invalid_email_data, format="json")
        self.assertEqual(response.status_code, 400)
