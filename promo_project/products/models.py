from django.db import models

<<<<<<< HEAD
class Product(models.Model):
    name = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)   
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
=======
# Create your models here.
>>>>>>> 29a63755d6a9a53d1586c88cc640e7b694ef106e
