from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(AbstractUser):
	rut = models.CharField(verbose_name='Rut', max_length=11)
	apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length=30)
	apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length=30)
	numero_contacto = models.IntegerField(verbose_name='Telefono Contacto', blank=True, null=True)
	direccion = models.CharField(verbose_name='Dirección', max_length=30)
