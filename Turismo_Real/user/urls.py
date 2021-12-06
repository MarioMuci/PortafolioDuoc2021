from django.urls import path
from user.views import *

urlpatterns = [
    path('ListadoUsuario/', UserListView.as_view(), name='listadousuario'),
    path('CrearUsuario/', UserCreateView.as_view(), name='crearusuario'),
    path('EditarUsuario/<int:pk>/', UserUpdateView.as_view(), name='editarusuario'),
    path('EditarMiPerfil/', UserProfileIndexViewClient.as_view(), name='editarmiperfil'),
    path('EliminarUsuario/<int:pk>/', UserDeleteView.as_view(), name='eliminarusuario'),
    path('EditarPerfil/', UserProfileView.as_view(), name='editarperfil'),
    path('MisDatos/', ProfileView.as_view(), name='misdatos'),
    path('EditarMiPerfil/', UserProfileIndexViewClient.as_view(), name='editarmiperfil'),
    path('EditarContraseña/', UserChangePasswordView.as_view(), name='editarcontraseña'),
    path('EditarMiContraseña/', UserChangeIndexPasswordView.as_view(), name='editarmicontraseña'),
]