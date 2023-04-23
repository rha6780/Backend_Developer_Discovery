from django.test.testcases import TestCase
from django.urls import reverse, resolve

from ..views import UserSignUpView, UserSignInView


class AccountUrlsTestCase(TestCase):
    def test_signup_url_is_resolved(self):
        url = reverse("sign-up")
        self.assertEquals(resolve(url).func.view_class, UserSignUpView)

    def test_signin_url_is_resolved(self):
        url = reverse("sign-in")
        self.assertEquals(resolve(url).func.view_class, UserSignInView)
