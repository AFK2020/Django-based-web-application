from django.test import TestCase
from django.urls import reverse
from django.test import Client
from unittest import mock
from django.contrib.auth import get_user_model
from myapp.models import CustomUser,Profile
from myapp.middleware.ip_logging import RateLimitMiddleware
from django.http import HttpResponseForbidden
from datetime import timedelta
from django.utils import timezone
from myapp.models import Profile  # Assuming you have a Profile model


class RateLimitMiddlewareTestCase(TestCase):
    def setUp(self):
        # Step 1: Create a mock userS
        # Step 1: Create a real user
        self.user = get_user_model().objects.create_user(
            email="testuser@gmail.GOLDcom", 
            password="password", 
            first_name='A', 
            last_name='K'
        )
        
        # Step 2: Create a real profile with default values for testing
        self.profile = Profile.objects.create(
            user=self.user,
            role="gold",  # Role determines the rate limit
            count=0,  # Number of requests made in the last time window
            hit_time=timezone.now() - timedelta(seconds=30)  # Set hit_time 30 seconds ago for testing
        )
        
        # Step 3: Log the user in
        self.client.login(email="testuser@gmail.com", password="password")
        


    def test_rate_limit_exceeded(self):
        self.profile.count = 10 # limit has exceeded
        response = self.client.get('/get-ip/')  # URL where rate limiting is applied
        
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.profile.count, 10)
        self.profile.save.assert_called_once()

    def test_rate_limit_not_exceeded(self):
        self.profile.count = 3 # limit has not exceeded
        response = self.client.get('/get-ip/')  # URL where rate limiting is applied
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.profile.count, 4)
        self.profile.save.assert_called_once()
