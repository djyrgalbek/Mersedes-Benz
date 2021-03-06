from django.contrib.auth.models import AbstractUser
from django.db import models


# Модель user'а
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.get_full_name()
