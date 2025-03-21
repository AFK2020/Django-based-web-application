from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db.models.signals import post_save
from django.dispatch import receiver

# from django.conf import settings


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, first_name, last_name, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(
        default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(
        default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(
        default=False
    )  # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Profile(models.Model):
    ROLE_CHOICES = [
        ("gold", "Gold"),
        ("silver", "Silver"),
        ("bronze", "Bronze"),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    ip_address = models.CharField(max_length=200, blank=True, null=True)
    hit_time = models.DateTimeField(blank=True, null=True, default=None)
    first_hit = models.DateTimeField(blank=True, null=True, default=None)


@receiver(post_save, sender=CustomUser)
def create_or_save_user_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
