from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from ..serializers import UserSignUpSerializer

User = get_user_model()


class UserSignUpSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer_class = UserSignUpSerializer
        cls.valid_data = {"email": "test1@test.com", "password": "test-password", "name": "test"}
        cls.invalid_email_data = {"email": "", "password": "test-password", "name": "test"}
        cls.invalid_password_data = {"email": "", "password": "test", "name": "test"}

    def test_validate_with_valid_data(self):
        serializer = self.serializer_class(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_validate_with_invalid_email_data(self):
        serializer = self.serializer_class(data=self.invalid_email_data)
        self.assertFalse(serializer.is_valid())

    def test_validate_with_invalid_password_data(self):
        serializer = self.serializer_class(data=self.invalid_password_data)
        self.assertFalse(serializer.is_valid())
