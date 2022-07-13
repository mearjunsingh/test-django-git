from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **kwargs):
        if not phone_number:
            raise ValueError("phone number not present")
        # email = self.normalize_email(email)

        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **kwargs):
        user = self.create_user(phone_number, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    # REQUIRED_FIELDS = ['phone_number']
    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
