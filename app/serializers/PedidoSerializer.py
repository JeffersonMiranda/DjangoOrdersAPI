from rest_framework import serializers
from app.models.Item import Item
from app.serializers.ItemSerializer import ItemSerializer
from app.models.Pedido import Pedido

class PedidoSerializer(serializers.ModelSerializer):
   
    itens = ItemSerializer(many = True)

    class Meta:
        model = Pedido
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': False}}

    def create(self, validated_data):
        pedido = validated_data
        itens = validated_data.pop('itens')

        novoPedido = Pedido.objects.create(**pedido)

        for item in itens:
            Item.objects.create(pedido = novoPedido, **item)

        return novoPedido

    def update(self,instance,validated_data):
        pedido = validated_data
        itens = validated_data.pop('itens')

        instance.cliente = pedido['cliente'] ## ATUALIZANDO O CLIENTE DO PEDIDO
        instance.save()
        
        itens_id = Item.objects.filter(pedido = instance).values_list('id',flat = True) ## RECUPERANDO OS IDS DOS ITENS NO BANCO DE DADOS
        id_itens = [] ## VARIÁVEL PARA GUARDAR OS IDS DO ITENS A SEREM ATUALIZADOS

        for item in itens:
            id_itens.append(item['id'])
            
        for id in itens_id: 
            if id not in id_itens:
                Item.objects.filter(id=id).delete() ## DELETANDO ITEM SE O MESMO NÃO ESTIVER ENTRE OS ELEMENTOS DA REQUEST  

        ## ATUALIZANDO OS DADOS DOS PEDIDOS           
        if itens:
            for i in itens:
                item_id = i.get('id',None) 
                if item_id: ## SE OBJETO JÁ EXISTE NO BANCO ENTÃO ALTERA
                    itemObject = Item.objects.get(id = item_id)
                    itemObject.produto = i['produto']
                    itemObject.quantidade = i['quantidade']
                    itemObject.precoUnitario = i['precoUnitario']
                    itemObject.save()
                else: ## SENÃO CRIA NOVA INSTANCIA
                    Item.objects.create(pedido = instance, **i)

        


        return instance
            
      
        

            
            



