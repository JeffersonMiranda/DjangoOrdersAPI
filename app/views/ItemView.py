from rest_framework import viewsets, status
from rest_framework.response import Response
from app import serializers
from app.models.Item import Item

class ItemView(viewsets.ModelViewSet):
    
    queryset = Item.objects.all()
    serializer_class =  serializers.ItemSerializer
