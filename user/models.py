import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
import random 
from django.forms import model_to_dict

class UserManager(BaseUserManager):
    def _create_user(self, username, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name,last_name, password=None, **extra_fields):
        return self._create_user(username, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, name,last_name, password=None, **extra_fields):
        return self._create_user(username, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    name = models.CharField('Nombres', max_length = 255, blank = False, null = False)
    last_name = models.CharField('Apellidos', max_length = 255, blank = False, null = False)
    phone_user = models.CharField('Telefono', max_length=50)
    dni = models.CharField('Documento', max_length=50, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['dni','name','last_name']

    def toJSON(self):
        item = model_to_dict(self)
        return item


    def _str_(self):
        return f'{self.name} {self.last_name}'