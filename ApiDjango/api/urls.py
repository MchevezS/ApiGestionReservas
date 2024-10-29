from django.urls import path, include
from . import views
from .views import ClientesListCreate, ClientesDetail, ClientesUpdate, ClientesDelete
from .views import Zonas_disponiblesListCreate, Zonas_disponiblesDetail, Zonas_disponiblesUpdate, Zonas_disponiblesDelete
from .views import Estado_reservaListCreate, Estado_reservaDetail, Estado_reservaUpdate, Estado_reservaDelete
from .views import ReservaListCreate, ReservaDetail, ReservaUpdate, ReservaDelete
from .views import Cancelar_reservaListCreate, Cancelar_reservaDetail, Cancelar_reservaUpdate, Cancelar_reservaDelete
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
# Rutas para los clientes
    path('clientes/',views.ClientesListCreate.as_view(), name='clientes-create'),
    path('clientes/<int:pk>/',views.ClientesDetail.as_view(), name='clientes-detail'),
    path('clientes/<int:pk>/',views.ClientesUpdate.as_view(), name='clientes-Update'),
    path('clientes/<int:pk>/',views.ClientesDelete.as_view(), name='clientes-delete'),
    
# Rutas para zonas disponibles
    path('zonas_disponibles/',views.Zonas_disponiblesListCreate.as_view(), name='zonas_disponibles-create'),
    path('zonas_disponiblles/<int:pk>/', views.Zonas_disponiblesDetail.as_view(), name='zonas_disponibles-detail'),
    path('zonas_disponibles/<int:pk>/',views.Zonas_disponiblesUpdate.as_view(), name='zonas_disponibles-Update'),
    path('zonas_disponibles/<int:pk>/',views.Zonas_disponiblesDelete.as_view(), name='zonas_disponibles-delete'),
    
# Rutas para los estados de reserva
    path('estado_reserva/',views.Estado_reservaListCreate.as_view(), name='estado_reserva-create'),
    path('estado_reserva/<int:pk>/',views.Estado_reservaDetail.as_view(), name='estado_reserva-detail'),
    path('estado_reserva/<int:pk>/',views.Estado_reservaUpdate.as_view(), name='estado_reserva-Update'),
    path('estado_reserva/<int:pk>/',views.Estado_reservaDelete.as_view(), name='estado_reserva-delete'),

# Rutas para las reservas
    path('reservas/',views. ReservaListCreate.as_view(), name='reservas-create'),
    path('reservas/<int:pk>/',views. ReservaDetail.as_view(), name='reservas-detail'),
    path('reservas/<int:pk>/',views.ReservaUpdate.as_view(), name='reservas-Update'),
    path('reservas/<int:pk>/',views.ReservaDelete.as_view(), name='reservas-delete'),

# Rutas Cancelar reserva
    path('cancelar_reserva/',views. Cancelar_reservaListCreate.as_view(), name='cancelar_reserva-create'),
    path('cancelar_reserva/<int:pk>/', views.Cancelar_reservaDetail.as_view(), name='cancelar_reserva-detail'),
    path('cancelar_reserva/<int:pk>/',views. Cancelar_reservaUpdate.as_view(), name='cancelar_reserva-Update'),
    path('cancelar_reserva/<int:pk>/',views. Cancelar_reservaDelete.as_view(), name='cancelar_reserva-delete'),
    
    
]