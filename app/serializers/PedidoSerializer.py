from rest_framework import serializers
from app.models.Pedido import Pedido

class PedidoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Pedido
        fields = '__all__'
    

