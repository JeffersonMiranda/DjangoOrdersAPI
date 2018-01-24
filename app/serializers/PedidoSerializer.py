from rest_framework import serializers
from app.models.Item import Item
from app.serializers.ItemSerializer import ItemSerializer
from app.models.Pedido import Pedido

class PedidoSerializer(serializers.ModelSerializer):
   
    itens = ItemSerializer(many = True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        pedido = validated_data
        itens = validated_data.pop('itens')

        novoPedido = Pedido.objects.create(**pedido)

        for item in itens:
            Item.objects.create(pedido = novoPedido, **item)

        return novoPedido

