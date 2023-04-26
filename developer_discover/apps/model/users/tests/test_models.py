from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from apps.model.users.tests.factories import UserFactory

User = get_user_model()


class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.email = "test1@test.com"
        cls.password = "test"

    def test_if_username_is_unique(self):
        before_count = 0
        User.objects.create(email=self.email, password=self.password)
        self.assertEqual(before_count + 1, User.objects.count())

    def test_if_not_username_is_unique_raise_error(self):
        User.objects.create(email=self.email, password=self.password)
        with self.assertRaises(IntegrityError):
            User.objects.create(email=self.email, password=self.password)
