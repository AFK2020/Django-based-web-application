from django.test import TestCase
import pdb
from django.test import Client
from unittest import mock
from django.contrib.auth import get_user_model
from myapp.middleware.ip_logging import RateLimitMiddleware
from django.http import HttpResponseForbidden
from myapp.models import CustomUser,Profile
import datetime
from django.utils import timezone


class RateLimitMiddlewareTestCase(TestCase):
    def setUp(self):
        # Step 1: Create a mock userS
        # Step 1: Create a real user
        self.user = get_user_model().objects.create_user(
            email="testuser@gmail.com", 
            password="password", 
            first_name='A', 
            last_name='K'
        )
        
        self.profile = self.user.profile
        self.profile.role = 'gold'
        self.profile.count = 0 
        self.profile.first_hit=timezone.now() - datetime.timedelta(seconds=30)
        self.profile.save()
        
        # Step 3: Log the user in
        self.client.login(email="testuser@gmail.com", password="password")
        


    def test_rate_limit_exceeded(self):
        self.profile.count = 10 # limit has exceeded

        self.profile.save()
        response = self.client.get('/get-ip/')  # URL where rate limiting is applied
        
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.profile.count, 10)

    def test_rate_limit_not_exceeded(self):
        self.profile.count = 3 # limit has not exceeded
        self.profile.save()

        response = self.client.get('/get-ip/')  # URL where rate limiting is applied
        self.assertEqual(response.status_code, 200)
        # get_object = CustomUser.objects.get(email= 'testuser@gmail.com')
        get_object = Profile.objects.get(user = self.user)
        self.assertEqual(get_object.count, 4)
    
    def test_unauthorized_user(self):
        self.client.logout()
        response = self.client.get('/get-ip/')  # URL where rate limiting is applied
        self.assertEqual(response.status_code, 302)
    

    def test_time_passed(self):
        self.profile.count = 10
        self.profile.first_hit = timezone.now() - datetime.timedelta(minutes=1)
        self.profile.save()
        self.profile = Profile.objects.get(user = self.user)

        response = self.client.get('/get-ip/')  # URL where rate limiting is applied
        self.assertEqual(response.status_code, 200)
        # get_object = CustomUser.objects.get(email= 'testuser@gmail.com')
        # get_object = Profile.objects.get(user = self.user)
        # self.assertEqual(get_object.count, 0)