from django.db import models
from app.models.Cliente import Cliente

class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    



