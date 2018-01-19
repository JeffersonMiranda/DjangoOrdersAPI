from django.db import models
from app.models.Item import Item

class Produto(models.Model):
    
    descricao = models.CharField(max_length = 50)
    precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)
    multiplo = models.IntegerField(null = True)


    ## BUSINESS LOGIC ##
    def possuiMultiplo(self): ## SE PRODUTO POSSUI MUTIPLO
        if (self.multiplo):
            return True
        return False

    def isMultiplo(self,Item): ## SE É MULTIPLO
        if self.possuiMultiplo():
            if (Item.quantidade % self.multiplo == 0):     
                return True  ## IS MULTIPLE
            return False ## NOT MULTIPLE
        return False ## NÃO POSSUI MÚLTIPLO
    ## BUSINESS LOGIC ##