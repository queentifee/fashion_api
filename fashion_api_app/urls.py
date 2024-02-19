from django.urls import path
from .views import (BrandListCreate, BrandRetrieveUpdateDestroy, CategoryListCreate, CategoryRetrieveUpdateDestroy, ProductListCreate, ProductRetrieveUpdateDestroy, ReviewListCreate, ReviewRetrieveUpdateDestroy)

urlpatterns = [
    path('brands/', BrandListCreate.as_view(), name='brand-list'),
    path('brand/<int:pk>/', BrandRetrieveUpdateDestroy.as_view(), name='brand-detail'),
    
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    
    path('reviews/', ReviewListCreate.as_view(), name='review-list'),
    path('product/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-detail'),
]
