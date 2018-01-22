from rest_framework import serializers
from app.models.Item import Item

class ItemSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Item
        fields = '__all__'
    

