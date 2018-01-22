from rest_framework import viewsets
from app import serializers
from app.models.Rentabilidade import Rentabilidade

class RentabilidadeView(viewsets.ModelViewSet):
    
    queryset = Rentabilidade.objects.all()
    serializer_class =  serializers.RentabilidadeSerializer


