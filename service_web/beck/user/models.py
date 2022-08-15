from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an phone number')
        user = self.model(
            phone_number=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        if not password:
            raise ValueError('staff/admins must have a password.')
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise ValueError('superusers must have a password.')
        user = self.create_user(email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    # email = models.EmailField(verbose_name='email address', max_length=255, db_index=True, unique=True)
    # username = models.CharField(max_length=254, null=True, blank=True,  unique=True)
    # last_name = models.CharField(max_length=64, null=True, blank=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # last_login = models.DateTimeField(null=True, blank=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # birthday = models.CharField(null=True, max_length=24, blank=True)
    # phone = models.CharField(unique=True, max_length=13, blank=True, null=True)
    # parent = models.CharField(max_length=12, blank=True, null=True)
    # uuid = models.CharField(max_length=100, unique=True, blank=True, null=True)
    # referrals_count = models.IntegerField(default=0, blank=True, null=True)
    # tg_id = models.IntegerField(default=0)
    # deposit_sum = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # withdraw_sum = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    #
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
    #
    # objects = UserManager()
    #
    # def __str__(self):
    #     return self.username
