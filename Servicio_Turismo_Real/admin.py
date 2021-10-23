from django.contrib import admin
from . models import ArticuloDepartamento, Cargo, CategoriaArticulo, CategoriaServicio, CheckIn, CheckOut, Departamento, DetalleCostoDepartamento, DetalleServicioAdicional, Funcionario, ImagenDepartamento, InventarioDepartamento, Mantenimiento, Reserva, ServicioAdicional, Zona

# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ["fun_rut", "fun_nombre", "fun_apellido_paterno", "f_car"]

admin.site.register(ArticuloDepartamento)
admin.site.register(Cargo)
admin.site.register(CategoriaArticulo)
admin.site.register(CategoriaServicio)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Departamento)
admin.site.register(DetalleCostoDepartamento)
admin.site.register(DetalleServicioAdicional)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(ImagenDepartamento)
admin.site.register(InventarioDepartamento)
admin.site.register(Mantenimiento)
admin.site.register(Reserva)
admin.site.register(ServicioAdicional)
admin.site.register(Zona)
