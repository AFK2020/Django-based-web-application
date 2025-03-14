from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import CustomUser, CustomUserManager, Profile
import json


class TestViews(TestCase):
#    def test_get_ip_unauthenticated_user(self):
#     response = self.client.get(reverse('get-ip'))
#     #  self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('get-ip')}")
#     self.assertEquals(response.status_code,302)

#    def test_get_ip_authenticated_user(self):
#     CustomUser.objects.create(email='test@gmail.com',password= '1234',first_name='A', last_name='K')
#     self.client.login(email='test@gmail.com',password= '1234')
#     response = self.client.get(reverse('get-ip'))
#     self.assertEquals(response.status_code,302)

    pass