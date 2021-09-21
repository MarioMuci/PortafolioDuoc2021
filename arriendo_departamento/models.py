# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArticuloDepartamento(models.Model):
    art_dep_id = models.IntegerField(primary_key=True)
    art_dep_fecha_ingreso = models.DateField()
    art_dep_nombre = models.CharField(max_length=30)
    art_dep_estado = models.CharField(max_length=1)
    art_dep_precio = models.IntegerField()
    f_cat_art = models.ForeignKey('CategoriaArticulo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'articulo_departamento'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_nombre = models.CharField(max_length=30)
    car_descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'cargo'


class CategoriaArticulo(models.Model):
    cat_art_id = models.IntegerField(primary_key=True)
    cat_art_nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'categoria_articulo'


class CategoriaServicio(models.Model):
    cat_ser_id = models.IntegerField(primary_key=True)
    cat_ser_nombre = models.CharField(max_length=15)
    cat_ser_descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'categoria_servicio'


class CheckIn(models.Model):
    check_in_id = models.IntegerField(primary_key=True)
    check_in_fecha = models.DateField()
    chek_in_observacion = models.CharField(max_length=300)
    f_res = models.ForeignKey('Reserva', models.DO_NOTHING)
    f_fun = models.ForeignKey('Funcionario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'check_in'


class CheckOut(models.Model):
    check_out_id = models.IntegerField(primary_key=True)
    check_out_fecha = models.DateField()
    check_out_observacion = models.CharField(max_length=300)
    check_out_multas = models.IntegerField()
    f_res = models.ForeignKey('Reserva', models.DO_NOTHING)
    f_fun = models.ForeignKey('Funcionario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'check_out'


class Cliente(models.Model):
    cli_id = models.IntegerField(primary_key=True)
    cli_rut = models.IntegerField()
    cli_rut_df = models.CharField(max_length=1)
    cli_nombre = models.CharField(max_length=30)
    cli_apellido_paterno = models.CharField(max_length=10)
    cli_apellido_materno = models.CharField(max_length=10)
    cli_numero_contacto = models.IntegerField()
    cli_ciudad = models.CharField(max_length=30)
    cli_comuna = models.CharField(max_length=30)
    cli_direccion = models.CharField(max_length=30)
    cli_email = models.CharField(max_length=30)
    cli_password = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cliente'


class Departamento(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_nombre = models.CharField(max_length=30)
    dep_ubicacion = models.CharField(max_length=30)
    dep_capacidad = models.IntegerField()
    dep_acondicionado = models.CharField(max_length=1)
    dep_canon_renta = models.IntegerField()
    dep_estado = models.CharField(max_length=1)
    dep_costo_mes = models.IntegerField()
    f_zona = models.ForeignKey('Zona', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departamento'


class DetalleCostoDepartamento(models.Model):
    des_cos_dep_dia = models.IntegerField()
    des_cos_dep_semanal = models.IntegerField()
    pf_dep = models.OneToOneField(Departamento, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'detalle_costo_departamento'


class DetalleServicioAdicional(models.Model):
    det_ser_fecha = models.DateField()
    det_ser_total = models.IntegerField()
    pf_res = models.OneToOneField('Reserva', models.DO_NOTHING, primary_key=True)
    pf_ser_adi = models.ForeignKey('ServicioAdicional', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'detalle_servicio_adicional'
        unique_together = (('pf_res', 'pf_ser_adi'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Funcionario(models.Model):
    fun_id = models.IntegerField(primary_key=True)
    fun_rut = models.IntegerField()
    fun_rut_df = models.CharField(max_length=1)
    fun_nombre = models.CharField(max_length=30)
    fun_apellido_paterno = models.CharField(max_length=30)
    fun_apellido_materno = models.CharField(max_length=30)
    fun_cargo = models.CharField(max_length=30)
    fun_usuario = models.CharField(max_length=30)
    fun_password = models.CharField(max_length=10)
    f_car = models.ForeignKey(Cargo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'funcionario'


class ImagenDepartamento(models.Model):
    ima_id = models.FloatField(primary_key=True)
    ima_departamento = models.BinaryField()
    f_dep = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'imagen_departamento'


class InventarioDepartamento(models.Model):
    pf_dep = models.OneToOneField(Departamento, models.DO_NOTHING, primary_key=True)
    pf_art_dep = models.ForeignKey(ArticuloDepartamento, models.DO_NOTHING)
    inv_dep_catidad = models.FloatField()
    inv_dep_costo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario_departamento'
        unique_together = (('pf_dep', 'pf_art_dep'),)


class Mantenimiento(models.Model):
    man_id = models.IntegerField(primary_key=True)
    man_fecha_creacion = models.DateField()
    man_fecha_desde = models.DateField()
    man_fecha_hasta = models.DateField()
    man_fecha_cancelacion = models.DateField()
    man_observacion = models.CharField(max_length=300)
    f_dep = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mantenimiento'


class Reserva(models.Model):
    res_id = models.IntegerField(primary_key=True)
    res_fecha = models.DateField()
    res_fecha_creacion = models.DateField()
    res_cantidad_huesped = models.FloatField()
    res_fecha_desde = models.DateField()
    res_fecha_hasta = models.DateField()
    res_fecha_cancelacion = models.DateField()
    res_total = models.IntegerField()
    res_pagada = models.CharField(max_length=1)
    f_dep = models.ForeignKey(Departamento, models.DO_NOTHING)
    f_cli = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reserva'


class ServicioAdicional(models.Model):
    ser_adi_id = models.IntegerField(primary_key=True)
    ser_adi_nombre = models.CharField(max_length=300)
    ser_adi_precio = models.FloatField()
    f_cat_ser = models.ForeignKey(CategoriaServicio, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servicio_adicional'


class Zona(models.Model):
    zona_id = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'zona'
