from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import get_user_ip, CustomLoginView, CustomLogoutView, RegisterPage

# import pytest

# Create your tests here.


# @pytest.mark.django_db
class TestUrls(SimpleTestCase):

    def test_get_ip_url(self):
        url = reverse("get-ip")
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_user_ip)

    def test_login_url(self):
        url = reverse("login")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)

    def test_logout_url(self):
        url = reverse("logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CustomLogoutView)

    def test_register_url(self):
        url = reverse("register")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterPage)
