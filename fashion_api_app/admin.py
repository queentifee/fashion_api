from django.contrib import admin
from .models import Brand, Review, Category, Product

admin.site.register(Brand) 
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)

