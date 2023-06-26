from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from unittest import mock

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
        response = self.client.post(reverse("sign-up"), self.invalid_password_data, format="json")
        self.assertEqual(response.status_code, 400)


class UserSignInViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create_user(email="test@test.com", password="test9090", name="test")

    def test_valid_data(self):
        valid_params_data = {"email": "test@test.com", "password": "test9090"}
        response = self.client.post(reverse("sign-in"), valid_params_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_not_exist_user_data(self):
        email_not_found_data = {"email": "test1@test.com", "password": "test9090"}
        response = self.client.post(reverse("sign-in"), email_not_found_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_invalid_password_data(self):
        invalid_password_data = {"email": "test@test.com", "password": "test9091"}
        response = self.client.post(reverse("sign-in"), invalid_password_data, format="json")
        self.assertEqual(response.status_code, 400)


class UserEmailConfirmView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create_user(email="test1@admin.com", password="test9090", name="test")

    def test_email_confirm(self):
        # TODO: invalid_email 해결하기
        with mock.patch("django.core.mail.send_mail") as mocked_mail:
            mocked_mail.side_effect = Exception("OH NOES")

        # valid_params_data = {"email": "test1@admin.com"}
        # response = self.client.post(reverse("email-check"), valid_params_data, format="json")
        # self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        invalid_params_data = {"email": "testtest.com"}
        response = self.client.post(reverse("email-confirm"), invalid_params_data, format="json")
        self.assertEqual(response.status_code, 400)
