from django.test.testcases import TestCase
from django.urls import reverse, resolve

from ..views import UserSignUpView, UserSignInView, UserEmailConfirmView, UserPasswordResetView


class AccountUrlsTestCase(TestCase):
    def test_signup_url_is_resolved(self):
        url = reverse("sign-up")
        self.assertEquals(resolve(url).func.view_class, UserSignUpView)

    def test_signin_url_is_resolved(self):
        url = reverse("sign-in")
        self.assertEquals(resolve(url).func.view_class, UserSignInView)

    def test_email_check_url_is_resolved(self):
        url = reverse("email-check")
        self.assertEquals(resolve(url).func.view_class, UserEmailConfirmView)

    def test_reset_password_url_is_resolved(self):
        url = reverse("reset-password")
        self.assertEquals(resolve(url).func.view_class, UserPasswordResetView)
