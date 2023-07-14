from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from unittest import mock
from unittest.mock import patch, MagicMock

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

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

    @patch("apps.api.v1.accounts.views.requests")
    def test_email_confirm(self, mocked_request):
        class FakeResponse:
            def json(self):
                return Response({"message": "Email Sending"}, status.HTTP_200_OK)

        mocked_request.get = MagicMock(return_value=FakeResponse())

        valid_params_data = {"email": "test1@admin.com"}
        response = self.client.post(reverse("email-confirm"), valid_params_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_email_not_found(self):
        invalid_params_data = {"email": "testtest.com"}
        response = self.client.post(reverse("email-confirm"), invalid_params_data, format="json")
        self.assertEqual(response.status_code, 404)


class UserResetPasswordView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create_user(email="test1@admin.com", password="test9090", name="test")
        cls.token, is_created = Token.objects.get_or_create(user=cls.user)

    def test_valid_data_reset_password_success(self):
        valid_params_data = {"token": str(self.token), "password": "test-8989"}
        response = self.client.post(reverse("reset-password"), valid_params_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_token_not_provide_reset_password_failed(self):
        invalid_params_data = {"token": "", "password": "test8989"}
        response = self.client.post(reverse("reset-password"), invalid_params_data, format="json")
        self.assertEqual(response.status_code, 404)

    def test_password_not_provide_reset_password_failed(self):
        invalid_params_data = {"token": str(self.token), "password": ""}
        response = self.client.post(reverse("reset-password"), invalid_params_data, format="json")
        self.assertEqual(response.status_code, 400)
