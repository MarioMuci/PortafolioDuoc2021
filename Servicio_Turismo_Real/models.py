# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from Turismo_Real.settings import MEDIA_URL, STATIC_URL
from base_model.base_model import BaseModel
from crum import get_current_user
from django.utils.translation import ugettext as _

class ArticuloDepartamento(BaseModel):
    art_dep_id = models.BigAutoField(primary_key=True)
    art_dep_fecha_ingreso = models.DateTimeField(auto_now=True)
    art_dep_nombre = models.CharField(verbose_name='Nombre', max_length=30)
    art_dep_estado = models.BooleanField(verbose_name='Estado')
    art_dep_precio = models.PositiveIntegerField(verbose_name='Precio', default=0)
    f_cat_art = models.ForeignKey('CategoriaArticulo', models.DO_NOTHING, verbose_name='Categoria')

    def __str__(self):
        return str(self.art_dep_nombre)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(ArticuloDepartamento, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['f_cat_art'] = self.f_cat_art.toJSON()
        return item

    class Meta:
        db_table = 'articulo_departamento'
        verbose_name = 'Articulo Departamento'
        verbose_name_plural = 'Articulos Departamentos'
        ordering = ['art_dep_id']


class Cargo(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    car_nombre = models.CharField(verbose_name='Nombre', max_length=30)
    car_descripcion = models.CharField(verbose_name='Descripción', max_length=150)

    def __str__(self):
        return str(self.car_nombre)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'cargo'


class CategoriaArticulo(models.Model):
    cat_art_id = models.BigAutoField(primary_key=True)
    cat_art_nombre = models.CharField(verbose_name='Nombre', unique=True, max_length=30)

    def __str__(self):
        return str(self.cat_art_nombre)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'categoria_articulo'
        verbose_name = 'Categoria Articulo'
        verbose_name_plural = 'Categoria Articulos'
        ordering = ['cat_art_id']


class CategoriaServicio(models.Model):
    cat_ser_id = models.BigAutoField(primary_key=True)
    cat_ser_nombre = models.CharField(verbose_name='Nombre', max_length=15)
    cat_ser_descripcion = models.CharField(verbose_name='Descripción', max_length=300)

    class Meta:
        db_table = 'categoria_servicio'


class CheckIn(models.Model):
    check_in_id = models.BigAutoField(primary_key=True)
    check_in_fecha = models.DateTimeField(verbose_name='Fecha', auto_now=True)
    chek_in_observacion = models.CharField(verbose_name='Observación', max_length=300)
    f_res = models.ForeignKey('Reserva', models.DO_NOTHING)
    f_fun = models.ForeignKey('Funcionario', models.DO_NOTHING)

    class Meta:
        db_table = 'check_in'


class CheckOut(models.Model):
    check_out_id = models.BigAutoField(primary_key=True)
    check_out_fecha = models.DateTimeField(verbose_name='Fecha', auto_now=True)
    check_out_observacion = models.CharField(verbose_name='Observación', max_length=300)
    check_out_multas = models.PositiveIntegerField(verbose_name='Multas' , default=0)
    f_res = models.ForeignKey('Reserva', models.DO_NOTHING)
    f_fun = models.ForeignKey('Funcionario', models.DO_NOTHING)

    class Meta:
        db_table = 'check_out'


class Departamento(BaseModel):
    dep_id = models.BigAutoField(primary_key=True)
    dep_nombre = models.CharField(verbose_name='Nombre', max_length=30)
    dep_ubicacion = models.CharField(verbose_name='Ubicación', max_length=30)
    dep_capacidad = models.PositiveIntegerField(verbose_name='Capacidad', default=0)
    dep_acondicionado = models.BooleanField(verbose_name='Acondicionado')
    dep_canon_renta = models.PositiveIntegerField(verbose_name='Renta', default=0)
    dep_estado = models.BooleanField(verbose_name='Estado')
    dep_costo_mes = models.PositiveIntegerField(verbose_name='Costo Mensual', default=0)
    dep_tipologia = models.CharField(verbose_name='Tipologia', max_length=5)
    dep_piso = models.PositiveIntegerField(verbose_name='Piso')
    dep_imagen_portada = models.ImageField(verbose_name='Portada', upload_to="media/departamentos")
    f_zona = models.ForeignKey('Zona', models.DO_NOTHING, verbose_name='Zona')

    def __str__(self):
        return str(self.dep_nombre)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Departamento, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['dep_imagen_portada'] = self.get_image()
        item['f_zona'] = self.f_zona.toJSON()
        return item

    def get_image(self):
        if self.dep_imagen_portada:
            return '{}{}'.format(MEDIA_URL, self.dep_imagen_portada)
        return '{}{}'.format(STATIC_URL, 'img/turismologopngicono.png')

    class Meta:
        db_table = 'departamento'


class DetalleCostoDepartamento(models.Model):
    des_cos_dep_dia = models.IntegerField(verbose_name='Costo Diario')
    des_cos_dep_semanal = models.IntegerField(verbose_name='Costo Semanal')
    pf_dep = models.OneToOneField(Departamento, models.DO_NOTHING, primary_key=True)

    class Meta:
        db_table = 'detalle_costo_departamento'


class DetalleServicioAdicional(models.Model):
    det_ser_fecha = models.DateTimeField(verbose_name='Fecha', auto_now=True)
    det_ser_total = models.IntegerField(verbose_name='Total')
    pf_res = models.OneToOneField('Reserva', models.DO_NOTHING, primary_key=True)
    pf_ser_adi = models.ForeignKey('ServicioAdicional', models.DO_NOTHING)

    class Meta:
        db_table = 'detalle_servicio_adicional'
        unique_together = (('pf_res', 'pf_ser_adi'),)


class Funcionario(BaseModel):
    fun_id = models.BigAutoField(primary_key=True)
    fun_rut = models.CharField(verbose_name='Rut', unique=True, max_length=10)
    fun_nombre = models.CharField(verbose_name='Nombre', max_length=30)
    fun_apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length=30)
    fun_apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length=30)
    f_car = models.ForeignKey(Cargo, models.DO_NOTHING, verbose_name='Categoria')

    def __str__(self):
        return str(self.fun_rut)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Funcionario, self).save()
        
    def toJSON(self):
        item = model_to_dict(self)
        item['f_car'] = self.f_car.toJSON()
        return item

    class Meta:
        db_table = 'funcionario'


class ImagenDepartamento(models.Model):
    ima_id = models.BigAutoField(primary_key=True)
    ima_departamento = models.ImageField(verbose_name='Imagenes Departamentos', upload_to="media/imagenes_departamentos")
    f_dep = models.ForeignKey(Departamento, models.DO_NOTHING)

    def __str__(self):
        return str(self.f_dep)

    def get_image(self):
        if self.ima_departamento:
            return '{}{}'.format(MEDIA_URL, self.ima_departamento)
        return '{}{}'.format(STATIC_URL, 'img/turismologopngicono.png')

    class Meta:
        db_table = 'imagen_departamento'


class InventarioDepartamento(models.Model):
    pf_dep = models.OneToOneField(Departamento, models.DO_NOTHING, primary_key=True)
    pf_art_dep = models.ForeignKey(ArticuloDepartamento, models.DO_NOTHING)
    inv_dep_cantidad = models.FloatField(verbose_name='Cantidad')
    inv_dep_costo = models.IntegerField(verbose_name='Costo')

    class Meta:
        db_table = 'inventario_departamento'
        unique_together = (('pf_dep', 'pf_art_dep'),)


class Mantenimiento(models.Model):
    man_id = models.BigAutoField(primary_key=True)
    man_fecha_creacion = models.DateTimeField(verbose_name='Fecha de Creación', auto_now=True)
    man_fecha_desde = models.DateField(verbose_name='Fecha Desde', default=datetime.now)
    man_fecha_hasta = models.DateField(verbose_name='Fecha Hasta', default=datetime.now)
    man_cancelacion = models.BooleanField(verbose_name='Cancelar Mantenimiento')
    man_observacion = models.CharField(max_length=300)
    f_dep = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        db_table = 'mantenimiento'


class Reserva(models.Model):
    res_id = models.BigAutoField(primary_key=True)
    res_fecha_creacion = models.DateTimeField(verbose_name='Fecha de Creación', auto_now=True)
    res_cantidad_huesped = models.FloatField(verbose_name='Cantidad de Huesped:')
    res_fecha_desde = models.DateField(verbose_name='Fecha Desde:', default=datetime.now)
    res_fecha_hasta = models.DateField(verbose_name='Fecha Hasta:', default=datetime.now)
    res_cancelacion = models.BooleanField(verbose_name='Cancelar Reserva:')
    res_total = models.IntegerField(verbose_name='Total:')
    res_pagada = models.BooleanField(verbose_name='Reserva Pagada:')
    f_dep = models.ForeignKey(Departamento, models.DO_NOTHING)
    f_cli = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        db_table = 'reserva'


class ServicioAdicional(models.Model):
    ser_adi_id = models.BigAutoField(primary_key=True)
    ser_adi_nombre = models.CharField(verbose_name='Nombre', max_length=300)
    ser_adi_precio = models.FloatField(verbose_name='Precio')
    f_cat_ser = models.ForeignKey(CategoriaServicio, models.DO_NOTHING)

    class Meta:
        db_table = 'servicio_adicional'


class UserUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(verbose_name='Contraseña', max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(verbose_name='Nombre de Usuario', unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(verbose_name='Nombre', max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    rut = models.CharField(verbose_name='Rut', unique=True, max_length=11, blank=True, null=True)
    apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length=30, blank=True, null=True)
    apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length=30, blank=True, null=True)
    numero_contacto = models.IntegerField(verbose_name='Numero de Contacto', blank=True, null=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

        permissions = (
            ('is_funcionario', _('Is Funcionario')),
            ('is_cliente', _('Is Cliente')),
        )


class Zona(models.Model):
    zona_id = models.CharField(verbose_name='Nombre', primary_key=True, max_length=15)

    def __str__(self):
        return str(self.zona_id)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'zona'









