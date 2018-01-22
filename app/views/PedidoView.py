from rest_framework import viewsets
from app import serializers
from app.models.Pedido import Pedido

class PedidoView(viewsets.ModelViewSet):
    
    queryset = Pedido.objects.all()
    serializer_class =  serializers.PedidoSerializer


