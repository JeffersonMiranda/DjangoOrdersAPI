from rest_framework import serializers
from app.serializers.ProdutoSerializer import ProdutoSerializer
from app.models.Item import Item

class ItemSerializer(serializers.ModelSerializer):
   
    produto = ProdutoSerializer(read_only=True)

    class Meta:
        model = Item
        exclude = ('rentabilidade','pedido')
    
    
