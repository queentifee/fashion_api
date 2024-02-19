from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    origin = models.CharField(max_length=50)
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    
    
def __str__(self):
        return self.name + ' ' + self.description

