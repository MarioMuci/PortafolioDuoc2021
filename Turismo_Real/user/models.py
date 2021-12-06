from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from django.utils.translation import ugettext as _

# Create your models here.
class User(AbstractUser):
	rut = models.CharField(verbose_name='Rut', unique=True, max_length=10)
	apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length=30)
	apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length=30)
	numero_contacto = models.IntegerField(verbose_name='Telefono Contacto', blank=True, null=True)
	direccion = models.CharField(verbose_name='Dirección', max_length=30)
	token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)

	class Meta:
		db_table = 'usuario'
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
		ordering = ['id']

		permissions = (
			('is_funcionario', _('Is Funcionario')),
			('is_cliente', _('Is Cliente')),
		)

	def __str__(self):
		return str(self.rut)

	def toJSON(self):
		item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
		if self.last_login:
			item['last_login'] = self.last_login.strftime('%Y-%m-%d')
		item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
		item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
		return item
