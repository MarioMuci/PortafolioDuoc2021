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
    path('Test/', TestView.as_view(), name='test'),
    path('Pronto/', ProntoView.as_view(), name='pronto'),
]