from rest_framework import viewsets
from app import serializers
from app.models.Cliente import Cliente

class ClienteView(viewsets.ModelViewSet):
    
    queryset = Cliente.objects.all()
    serializer_class =  serializers.ClienteSerializer


