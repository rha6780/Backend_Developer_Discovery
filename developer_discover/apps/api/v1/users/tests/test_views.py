from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class CurrentUserViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create_user(email="test@test.com", password="test9090", name="test")

    def test_user_is_not_exist(self):
        res = self.client.get(reverse("current"), format="json")
        self.assertEqual(res.status_code, 401)

    def test_user_is_exist(self):
        client = APIClient()
        request_factory = APIRequestFactory()
        refresh = RefreshToken.for_user(self.user)
        request = request_factory.get(reverse("email"))

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = client.get(reverse("current"), format="json")
        force_authenticate(request, user=self.user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"id": self.user.id, "email": "test@test.com", "name": "test"})


# https://stackoverflow.com/questions/47576635/django-rest-framework-jwt-unit-test
class ChangeEmailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request_factory = APIRequestFactory()
        cls.user = User.objects.create_user(email="test@test.com", password="test9090", name="test")
        cls.valid_email_data = {"changed_email": "test1@test.com"}
        cls.invalid_email_data = {"changed_email": ""}

    def test_valid_email_data(self):
        client = APIClient()
        request = self.request_factory.post(reverse("email"))
        refresh = RefreshToken.for_user(self.user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = client.patch(reverse("email"), self.valid_email_data, format="json")
        force_authenticate(request, user=self.user)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.email, "test1@test.com")

    def test_invalid_email_data(self):
        client = APIClient()
        request = self.request_factory.post(reverse("email"))
        refresh = RefreshToken.for_user(self.user)

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = client.patch(reverse("email"), self.invalid_email_data, format="json")
        force_authenticate(request, user=self.user)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.user.email, "test@test.com")


# TODO: 로직, url 추가 후 작성
# class ChangePasswordViewTestCase(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.request_factory = APIRequestFactory()
#         cls.user = User.objects.create_user(email="test@test.com", password="test9090", name="test")
#         cls.valid_email_data = {"password": "test1@test.com"}
#         cls.invalid_email_data = {"password": ""}
