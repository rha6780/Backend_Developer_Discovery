from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.core.exceptions import (
    ValidationError,
)

from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


# https://stackoverflow.com/questions/47576635/django-rest-framework-jwt-unit-test
class UserViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request_factory = APIRequestFactory()
        cls.user = User.objects.create_user(email="test@test.com", password="test9090", name="test")
        cls.valid_changed_data = {"changed_email": "test1@test.com", "changed_name": "test"}
        cls.invalid_changed_data = {"changed_email": "", "changed_name": ""}

    def test_user_is_not_exist(self):
        res = self.client.get(reverse("user"), format="json")
        self.assertEqual(res.status_code, 401)

    def test_user_is_exist(self):
        client = APIClient()
        request_factory = APIRequestFactory()
        refresh = RefreshToken.for_user(self.user)
        request = request_factory.get(reverse("user"))

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = client.get(reverse("user"), format="json")
        force_authenticate(request, user=self.user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, {"id": self.user.id, "email": "test@test.com", "name": "test", "image": "/user_icon.png"}
        )

    def test_valid_changed_data(self):
        client = APIClient()
        request = self.request_factory.post(reverse("user"))
        refresh = RefreshToken.for_user(self.user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = client.patch(reverse("user"), self.valid_changed_data, format="json")
        force_authenticate(request, user=self.user)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.email, "test1@test.com")

    def test_invalid_changed_data(self):
        client = APIClient()
        request = self.request_factory.post(reverse("user"))
        refresh = RefreshToken.for_user(self.user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = client.patch(reverse("user"), self.invalid_changed_data, format="json")
        force_authenticate(request, user=self.user)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.user.email, "test@test.com")


class ChangePasswordViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request_factory = APIRequestFactory()
        cls.user = User.objects.create_user(email="test@test.com", password="test-9090test", name="test")
        cls.valid_password_data = {"changed_password": "test-8989test"}
        cls.invalid_password_data = {"changed_password": ""}

    def test_change_password_with_valid_password(self):
        client = APIClient()
        request = self.request_factory.post(reverse("password"))
        refresh = RefreshToken.for_user(self.user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = client.patch(reverse("password"), self.valid_password_data, format="json")
        force_authenticate(request, user=self.user)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.check_password("test-8989test"), True)

    def test_change_password_with_invalid_password(self):
        client = APIClient()
        request = self.request_factory.post(reverse("password"))
        refresh = RefreshToken.for_user(self.user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        response = client.patch(reverse("password"), self.invalid_password_data, format="json")
        force_authenticate(request, user=self.user)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 400)
