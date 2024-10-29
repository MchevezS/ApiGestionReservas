from django.shortcuts import render
from .models import Clientes, Zonas_disponibles, Estado_reserva, Reserva, Cancelar_reserva
from .serializers import ClientesSerializer, Zonas_disponiblesSerializer, Estado_reservaSerializer, ReservaSerializer, Cancelar_reservaSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ClientesDelail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Clientes.objects.all()
   serializer_class = ClientesSerializer
   permission_classes = [IsAuthenticated] 


# Creacion de views de Clientes#(metodos)

class ClientesListCreate(generics.ListCreateAPIView):  #POST
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    

class ClientesDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class ClientesUpdate(generics.UpdateAPIView): # UPDATE
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    lookup_field = 'id'
    
class ClientesDelete(generics.UpdateAPIView): # DELETE
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    lookup_field = 'id'
    
    

# Creacion de views de Zonas disponibles(metodos).
class Zonas_disponiblesListCreate(generics.ListCreateAPIView):  #POST
    queryset = Zonas_disponibles.objects.all()
    serializer_class = Zonas_disponiblesSerializer
    

class Zonas_disponiblesDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Zonas_disponibles.objects.all()
    serializer_class = Zonas_disponiblesSerializer

class Zonas_disponiblesUpdate(generics.UpdateAPIView): # UPDATE
    queryset = Zonas_disponibles.objects.all()
    serializer_class = Zonas_disponiblesSerializer
    lookup_field = 'id'
    
class Zonas_disponiblesDelete(generics.UpdateAPIView): # DELETE
    queryset = Zonas_disponibles.objects.all()
    serializer_class = Zonas_disponiblesSerializer
    lookup_field = 'id'
    

# Creacion de views de Estado_reserva(metodos).
class Estado_reservaListCreate(generics.ListCreateAPIView):  #POST
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer
    

class Estado_reservaDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer

class Estado_reservaUpdate(generics.UpdateAPIView): # UPDATE
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer
    lookup_field = 'id'
    
class Estado_reservaDelete(generics.UpdateAPIView): # DELETE
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer
    lookup_field = 'id'
    

# Creacion de views de Reserva(metodos).
class ReservaListCreate(generics.ListCreateAPIView):  #POST
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaUpdate(generics.UpdateAPIView): # UPDATE
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    lookup_field = 'id'
    
class  ReservaDelete(generics.UpdateAPIView): # DELETE
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    lookup_field = 'id'
  
  
# Creacion de views de Reserva(metodos).
class Cancelar_reservaListCreate(generics.ListCreateAPIView):  #POST
    queryset = Cancelar_reserva.objects.all()
    serializer_class = ReservaSerializer
    

class Cancelar_reservaDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Cancelar_reserva.objects.all()
    serializer_class = Cancelar_reservaSerializer

class Cancelar_reservaUpdate(generics.UpdateAPIView): # UPDATE
    queryset = Cancelar_reserva.objects.all()
    serializer_class = Cancelar_reservaSerializer
    lookup_field = 'id'
    
class  Cancelar_reservaDelete(generics.UpdateAPIView): # DELETE
    queryset = Cancelar_reserva.objects.all()
    serializer_class = Cancelar_reservaSerializer
    lookup_field = 'id'
    