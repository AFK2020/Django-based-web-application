from django.test import TestCase
from django.urls import reverse
from myapp.models import CustomUser


class TestViews(TestCase):
    #   def test_get_ip_unauthenticated_user(self):
    #     response = self.client.get(reverse('get-ip'))
    #     #  self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('get-ip')}")
    #     self.assertEquals(response.status_code,302)
    login_url = "/login/"

    def setUp(self):
        CustomUser.objects.create(
            email="test@gmail.com", password="1234", first_name="A", last_name="K"
        )

    def test_get_ip_authenticated_user(self):
        self.client.login(email="test@gmail.com", password="1234")
        response = self.client.get(reverse("get-ip"))
        self.assertEquals(response.status_code, 302)

    def test_login_valid_user(self):
        response = self.client.post(
            self.login_url, {"email": "test@gmail.com", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_user(self):
        response = self.client.post(
            self.login_url, {"email": "testuser", "password": "wrongpassword"}
        )
        self.assertTemplateUsed(response, "myapp/login.html")
