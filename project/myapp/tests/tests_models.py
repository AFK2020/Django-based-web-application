from django.test import TestCase
from myapp.models import CustomUser,Profile
from django.contrib.auth import get_user_model


class MyTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com',password= '1234',first_name='A', last_name='K')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@gmail.com')

    def test_profile(self):
        self.assertEqual(self.user.profile.hit_time, None)
    
    def test_create_user_in_Manager(self):
        self.assertEqual(self.user.email, "test@gmail.com")
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(self.user.username)
        except AttributeError:
            pass

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo", first_name='S', last_name='F')
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass