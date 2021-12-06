from django.urls import path
from Servicio_Turismo_Real.views import *

urlpatterns = [
    path('Home/', HomeView.as_view(), name='home'),
    path('ListadoArticulo/', ArticuloDepartamentoListView.as_view(), name='listadoarticulo'),
    path('CrearArticulo/', ArticuloDepartamentoCreateView.as_view(), name='creararticulo'),
    path('EditarArticulo/<int:pk>/', ArticuloDepartamentoUpdateView.as_view(), name='editararticulo'),
    path('EliminarArticulo/<int:pk>/', ArticuloDepartamentoDeleteView.as_view(), name='eliminararticulo'),
    path('ListadoDepartamento/', DepartamentoListView.as_view(), name='listadodepartamento'),
    path('CrearDepartamento/', DepartamentoCreateView.as_view(), name='creardepartamento'),
    path('EditarDepartamento/<int:pk>/', DepartamentoUpdateView.as_view(), name='editardepartamento'),
    path('EliminarDepartamento/<int:pk>/', DepartamentoDeleteView.as_view(), name='eliminardepartamento'),
    path('ImagenesDepartamentos/', ImagenDepartamentoListView.as_view(), name='imagenesdepartamentos'),
    path('ListadoFuncionario/', FuncionarioView.as_view(), name='listadofuncionario'),
    path('CrearDetalleCostoDepartamento/', DetalleCostoDepartamentoView.as_view(), name='detallecostodepartamento'),
    path('ListadoDetalleCostoDepartamento/', DetalleCostoDepartamentoListView.as_view(), name='listadetallecostodepartamento'),
    path('EditarDetalleCostoDepartamento/<int:pk>/', DetalleCostoDepartamentoUpdateView.as_view(), name='editardetallecostodepartamento'),
    path('EliminarDetalleCostoDepartamento/<int:pk>/', DetalleCostoDepartamentoDeleteView.as_view(), name='eliminardetallecostodepartamento'),
    path('DetalleCostoDepartamentoPdf/<int:pk>/', DetalleCostoDepartamentoPdfView.as_view(), name='detallecostodepartamentopdf'),
    path('ListadoDepartamentosDisponibles/', ListadoDepartamentosDisponibles.as_view(), name='listadodepartamentosdisponibles'),
    path('DetalleDepartamentosDisponibles/<int:pk>/', DetalleDepartamentosDisponibles.as_view(), name='detalledepartamentosdisponibles'),
    path('RegistrarReserva/', RegistrarReserva.as_view(), name='registrarreserva'),
]