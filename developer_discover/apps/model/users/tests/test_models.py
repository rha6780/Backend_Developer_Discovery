from django.test import TestCase

from django.contrib.auth import get_user_model
from apps.model.users.tests.factories import UserFactory

User = get_user_model()


class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.email = "test@github.com"
        cls.password = "test"
