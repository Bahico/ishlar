from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.db.models.signals import post_save

# from config import settings


class UserManager(BaseUserManager):
    def create_user(self, phone_number, last_name, first_name, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        return user

    def create_staffuser(self, phone_number, last_name, first_name, password):
        if not password:
            raise ValueError('staff/admins must have a password.')
        user = self.create_user(phone_number, last_name, first_name, password=password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, phone_number, last_name, first_name, password=None):
        print(phone_number, last_name, first_name, password)
        if not password:
            raise ValueError('superusers must have a password.')
        user = self.create_user(phone_number, last_name, first_name, password=password)
        user.last_name = last_name
        user.first_name = first_name
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, unique=True,
                                max_length=24)  # shu ishlamasaxam turishi kerak ekan
    phone_number = models.CharField(max_length=13, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user_image", blank=True)
    description = models.TextField(blank=True)
    password = models.CharField(max_length=100)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'image', 'description']

    objects = UserManager()

    def __str__(self):
        return self.last_name


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
