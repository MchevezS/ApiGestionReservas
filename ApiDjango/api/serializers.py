from rest_framework import serializers

from .models import Clientes
from .models import Zonas_disponibles
from .models import Estado_reserva
from .models import Reserva
from .models import Cancelar_reserva


# convierte los datos como objetos de una base de datos

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        
class Zonas_disponiblesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Zonas_disponibles
        fields = '_all_'
        
        
class Estado_reservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_reserva
        fields = '_all_'
        
        
class ReservaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Reserva
        fields = '_all_'
        
        
class Cancelar_reservaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Cancelar_reserva
        fields = '_all_'  
        
        
        
        
        