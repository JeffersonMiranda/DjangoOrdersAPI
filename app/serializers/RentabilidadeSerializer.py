from rest_framework import serializers
from app.models.Rentabilidade import Rentabilidade

class RentabilidadeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Rentabilidade
        fields = '__all__'
    

