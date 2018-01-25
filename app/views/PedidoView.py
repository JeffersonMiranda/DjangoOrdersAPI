from rest_framework import viewsets, status
from app.serializers.ProdutoSerializer import ProdutoSerializer
from _decimal import Decimal
from app.models.Produto import Produto
from app.serializers.PedidoSerializer import PedidoSerializer
from app.models.Item import Item
from app.serializers.ItemSerializer import ItemSerializer
from rest_framework.response import Response
from app import serializers
from app.models.Pedido import Pedido

class PedidoView(viewsets.ModelViewSet):
    
    queryset = Pedido.objects.all()
    serializer_class =  serializers.PedidoSerializer

    def create(self, request):

        pedidoData = request.data

        serializerPedido = PedidoSerializer(data = pedidoData)
        if serializerPedido.is_valid():
          
            for i in pedidoData['itens']:            
                serializerItem = ItemSerializer(data = i)
                
                if serializerItem.is_valid():    
                    item = Item()                 
                    item.quantidade = serializerItem.data['quantidade']
                    item.precoUnitario = Decimal(serializerItem.data['precoUnitario'])
                    item.produto = Produto.objects.get(id = serializerItem.data['produto'])

                    ## APLICAÇÃO DAS REGRAS DE NEGÓCIOS
                    if item.produto.possuiMultiplo(): ## SE O PRODUTO POSSUI MULTIPLO PARA SER CALCULADO
                        if not item.produto.isMultiplo(item):
                            return Response({'ErrorMsg':'O produto '+ item.produto.descricao + ' só pode ser vendido em quantidades múltiplas de '+ str(item.produto.multiplo) +' !'}, status = status.HTTP_406_NOT_ACCEPTABLE)                    
                    if not  (item.isPrecoMaiorZero()):
                        return Response({'ErrorMsg':'Preços precisam ser maior do que zero e conter dois decimais !'}, status = status.HTTP_406_NOT_ACCEPTABLE)
                    if not (item.isQuantidadeMaiorZero()):
                        return Response({'ErrorMsg': 'Quantidades devem ser maiores do que zero !'}, status = status.HTTP_406_NOT_ACCEPTABLE)
                    if not (item.calcRentabilidade()):
                        return Response({'ErrorMsg': 'Rentabilidade não pode ser ruim !'}, status = status.HTTP_406_NOT_ACCEPTABLE)                   
                        
                else:
                    return Response({"ErrorMsg":serializerItem.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

            ## SE O OBJETO SEGUIU AS REGRAS DE NEGÓCIOS CORRETAMENTE, ENTÃO SALVA O PEDIDO COM ITENS NO BANCO :::
            serializerPedido.save()

        else:
            return Response({"ErrorMsg": serializerPedido.errors} ,status=status.HTTP_406_NOT_ACCEPTABLE)        
       
        return Response({"data":serializerPedido.data},status = status.HTTP_201_CREATED)

