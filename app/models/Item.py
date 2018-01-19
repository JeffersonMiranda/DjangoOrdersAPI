from django.db import models
from Pedido import Pedido
from Produto import Produto

class Item(models.Model):
    
    ''' RENTABILIDADE 
        1 => Ótima
        2 => Boa
        3 => Ruim        
    '''
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    quantidade = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)
    rentabilidade = models.CharField(max_length = 10)

   
    def isPrecoMaiorZero(self): ## DEFINE SE PREÇO É MAIOR QUE ZERO
        if (self.precoUnitario > 0) & (self.precoUnitario[::-1].find('.') == 2): 
            return True
        return False

    def isQuantidadeMaiorZero(self): ## DEFINE SE QUANTIDADE É INTEIRO E MAIOR QUE ZERO 
        if (isinstance(self.quantidade,int)) & (self.quantidade > 0):
            return True
        return False
     
    ## BUSINESS LOGIC ##
    def calcRentabilidade(self): ## CALCULAR RENTABILIDADE
        precoItem, precoProd = self.produto.precoUnitario, self.precoUnitario ## VERY COOL, RIGHT ?
        precoProd10Percent = precoProd % 10;  ## RETORNA 10% DO PREÇO DO PRODUTO

        if ( precoItem > precoProd): 
            self.rentabilidade = 1
            return True  ## RETORNA TRUE SE RENTABILIDADE FOR ÓTIMA
        elif (precoItem >= (precoProd - precoProd10Percent) & precoItem <= precoProd):
            self.rentabilidade = 2
            return True  ## RETORNA TRUE SE RENTABILIDADE FOR BOA
        elif (precoItem < precoProd):
            self.rentabilidade = 3
            return False  ## RETORNA FALSE SE RENTABILIDADE FOR RUIM E CANCELA CADASTRO DO ITEM
    ## BUSINESS LOGIC ##


     


