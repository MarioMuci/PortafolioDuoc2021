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
from user.models import User

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
    dep_ocupacion = models.SmallIntegerField(verbose_name ='Stock', default = 1)
    dep_estado = models.BooleanField(verbose_name='Disponibilidad')
    dep_costo_mes = models.PositiveIntegerField(verbose_name='Costo Mensual', default=0)
    dep_tipologia = models.CharField(verbose_name='Tipologia', max_length=10)
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
    des_cos_fecha_ingreso = models.DateTimeField(auto_now=True)
    des_cos_dep_dia = models.IntegerField(verbose_name='Costo Diario', default=0)
    des_cos_dep_semanal = models.IntegerField(verbose_name='Costo Semanal', default=0)
    pf_fun = models.ForeignKey('Funcionario', models.DO_NOTHING)

    def toJSON(self):
        item = model_to_dict(self)
        item['des_cos_fecha_ingreso'] = self.des_cos_fecha_ingreso.strftime('%Y-%m-%d')
        item['pf_fun'] = self.pf_fun.toJSON()
        item['det'] = [i.toJSON() for i in self.costodepartamento_set.all()]
        return item

    class Meta:
        db_table = 'detalle_costo_departamento'

class CostoDepartamento(models.Model):
    des_cos = models.ForeignKey(DetalleCostoDepartamento, on_delete=models.CASCADE)
    dep = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cos_mensual = models.IntegerField(default=0)
    cos_cant = models.IntegerField(default=0)
    cos_subtotal = models.IntegerField(default=0)

    def toJSON(self):
        item = model_to_dict(self, exclude=['des_cos'])
        item['dep'] = self.dep.toJSON()
        return item

    class Meta:
        db_table = 'costo_departamento'

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
    f_car = models.ForeignKey(Cargo, models.DO_NOTHING, verbose_name='Cargo')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {} {}'.format(self.fun_nombre, self.fun_apellido_paterno, self.fun_apellido_materno)


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
        item['full_name'] = self.get_full_name()
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
    res_cantidad_huesped = models.FloatField(verbose_name='Cantidad de Huesped', default=1)
    res_cantidad_diad = models.SmallIntegerField(verbose_name ='Cantidad de Dias', default=1)
    res_estado = models.BooleanField(verbose_name='Cancelar Reserva', default=False)
    res_total = models.IntegerField(verbose_name='Total', default=0)
    res_pagada = models.BooleanField(verbose_name='Reserva Pagada', default=False)
    f_dep = models.ForeignKey(Departamento, models.DO_NOTHING)
    f_use = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        db_table = 'reserva'


class ServicioAdicional(models.Model):
    ser_adi_id = models.BigAutoField(primary_key=True)
    ser_adi_nombre = models.CharField(verbose_name='Nombre', max_length=300)
    ser_adi_precio = models.FloatField(verbose_name='Precio')
    f_cat_ser = models.ForeignKey(CategoriaServicio, models.DO_NOTHING)

    class Meta:
        db_table = 'servicio_adicional'

class Zona(models.Model):
    zona_id = models.BigAutoField(primary_key=True)
    zona_nombre = models.CharField(verbose_name='Nombre', max_length=30)

    def __str__(self):
        return str(self.zona_nombre)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'zona'









