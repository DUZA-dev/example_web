from django.db import models, transaction
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from event.models import Organization

class UserRestManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Установите email')
        try:
            with transaction.atomic():
                user = self.model(email=email, password=password, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=35, unique=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    organizations = models.ManyToManyField(Organization, related_name="users")

    objects = UserRestManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    #def save(self, *args, **kwargs):
    #    super(User, self).save(*args, **kwargs)
    #    return self


