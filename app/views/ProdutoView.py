from rest_framework import viewsets
from app import serializers
from app.models.Produto import Produto

class ProdutoView(viewsets.ModelViewSet):
    
    queryset = Produto.objects.all()
    serializer_class =  serializers.ProdutoSerializer


