from django.urls import path
from .views import ClothingItemListCreate, ClothingItemRetrieveUpdateDestroy

urlpatterns = [
    path('clothing/', ClothingItemListCreate.as_view(), name='clothing-list-create'),
    path('clothing/<int:pk>/', ClothingItemRetrieveUpdateDestroy.as_view(), name='clothing-detail'),
]
