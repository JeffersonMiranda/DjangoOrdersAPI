from django.db import models
from app.models.Pedido import Pedido
from app.models.Produto import Produto
from decimal import Decimal

class Item(models.Model):
    
    ''' RENTABILIDADE 
        1 => Ótima
        2 => Boa
        3 => Ruim        
    '''

    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE, related_name = 'itens')
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    quantidade = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)
    rentabilidade = models.CharField(max_length = 10)

   
    def isPrecoMaiorZero(self): ## DEFINE SE PREÇO É MAIOR QUE ZERO
        precoCasasDecimais = len(str(self.precoUnitario).rsplit(".",1)[-1])    
        if (self.precoUnitario > 0) & (precoCasasDecimais <= 2): 
            return True
        return False

    def isQuantidadeMaiorZero(self): ## DEFINE SE QUANTIDADE É INTEIRO E MAIOR QUE ZERO 
        if (isinstance(self.quantidade,int)) & (self.quantidade > 0):
            return True
        return False
     
    ## BUSINESS LOGIC ##
    def calcRentabilidade(self): ## CALCULAR RENTABILIDADE
        precoProd,precoItem = self.produto.precoUnitario, self.precoUnitario ## VERY COOL, RIGHT ?
        precoProd10Percent = precoProd % 10;  ## RETORNA 10% DO PREÇO DO PRODUTO

        if ( precoItem > precoProd): 
            self.rentabilidade = 1
            return True  ## RETORNA TRUE SE RENTABILIDADE FOR ÓTIMA
        elif (precoItem >= (precoProd - precoProd10Percent) and precoItem <= precoProd):
            self.rentabilidade = 2
            return True  ## RETORNA TRUE SE RENTABILIDADE FOR BOA
        elif (precoItem < precoProd):
            self.rentabilidade = 3
            return False  ## RETORNA FALSE SE RENTABILIDADE FOR RUIM E CANCELA CADASTRO DO ITEM
    ## BUSINESS LOGIC ##


     


