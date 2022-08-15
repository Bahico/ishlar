from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        user = self.model(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, phone_number, password):
        if not password:
            raise ValueError('staff/admins must have a password.')
        user = self.create_user(phone_number, password=password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, phone_number, last_name, first_name, password=None):
        if not password:
            raise ValueError('superusers must have a password.')
        user = self.create_user(phone_number, password=password)
        user.last_name = last_name
        user.first_name = first_name
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['last_name', 'first_name']

    objects = UserManager()
