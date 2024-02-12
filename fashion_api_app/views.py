from rest_framework import generics
from .models import ClothingItem
from .serializers import ClothingItemSerializer


class ClothingItemListCreate(generics.ListCreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
    
class ClothingItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset = ClothingItem.objects.all()
     serializer_class = ClothingItemSerializer

