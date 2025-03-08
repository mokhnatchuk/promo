from django.db import models

<<<<<<< HEAD
class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=512) 
    city = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
=======
# Create your models here.
>>>>>>> 29a63755d6a9a53d1586c88cc640e7b694ef106e
