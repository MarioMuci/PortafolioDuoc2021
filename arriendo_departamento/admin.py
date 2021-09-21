from django.contrib import admin

# Register your models here.
from . models import ArticuloDepartamento, Cargo, CategoriaArticulo, CategoriaServicio, CheckIn, CheckOut, Cliente, Departamento, DetalleCostoDepartamento, DetalleServicioAdicional, Funcionario, ImagenDepartamento, InventarioDepartamento, Mantenimiento, Reserva, ServicioAdicional, Zona

admin.site.register(ArticuloDepartamento)
admin.site.register(Cargo)
admin.site.register(CategoriaArticulo)
admin.site.register(CategoriaServicio)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Cliente)
admin.site.register(Departamento)
admin.site.register(DetalleCostoDepartamento)
admin.site.register(DetalleServicioAdicional)
admin.site.register(Funcionario)
admin.site.register(ImagenDepartamento)
admin.site.register(InventarioDepartamento)
admin.site.register(Mantenimiento)
admin.site.register(Reserva)
admin.site.register(ServicioAdicional)
admin.site.register(Zona)

