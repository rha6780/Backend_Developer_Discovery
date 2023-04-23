from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "test1"
        cls.password = "test"
        cls.user = User.objects.create(username=cls.username, password=cls.password)
