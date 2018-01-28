from rest_framework import serializers
from app.models.Produto import Produto
from app.serializers.ProdutoSerializer import ProdutoSerializer
from app.models.Item import Item

class ItemSerializer(serializers.ModelSerializer):
   
    produto = ProdutoSerializer(read_only = True)
    produto_id = serializers.PrimaryKeyRelatedField(write_only=True,source='produto',queryset = Produto.objects.all())

    class Meta:
        model = Item
        exclude = ('rentabilidade','pedido')
        extra_kwargs = {'id': {'read_only': False}}
   