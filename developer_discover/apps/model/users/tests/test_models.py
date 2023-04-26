from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from apps.model.users.tests.factories import UserFactory

User = get_user_model()


class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.email = "test1@test.com"
        cls.name = "test"
        cls.password = "dsgjkeg9"

    def test_if_username_is_unique(self):
        before_count = 0
        User.objects.create_user(email=self.email, password=self.password, name=self.name)
        self.assertEqual(before_count + 1, User.objects.count())

    def test_if_not_username_is_unique_raise_error(self):
        User.objects.create_user(email=self.email, password=self.password, name=self.name)
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email=self.email, password=self.password, name=self.name)

    def test_password_validate(self):
        with self.assertRaises(ValidationError):
            User.objects.create_user(email=self.email, password="", name=self.name)
