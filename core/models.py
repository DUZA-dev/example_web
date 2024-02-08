from django.db import models, transaction
from django.contrib.auth.models import UserManager, User
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from event.models import Organization


class UserRestManager(UserManager):
    """
    Манага для модели User, переопределяет стандартные
    методы создания пользователя и админа, трыцпыцпыц
    """
    def create_user(self, email: str, password: str, **extra_fields) -> User:
        if not email:
            raise ValueError('Установите email')
        try:
            with transaction.atomic():
                user = self.model(email=email, password=password, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise ConnectionError('Произошла ошибка при создании пользователя.')

    def create_superuser(self, email: str, password: str, **extra_fields) -> User:
        """
        Не забываем переопределить метод создания уважаемых админов,
        установка нужных флагов is_staff & is_superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Переопределенная модель пользователя, добавлена связь с организациями,
    добавил поле телефонного номера и переопределил поле username по умолчанию на email
    """
    email = models.EmailField(max_length=35, unique=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    organizations = models.ManyToManyField(Organization, related_name="users")

    objects = UserRestManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
