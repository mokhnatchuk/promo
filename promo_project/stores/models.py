from django.db import models

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
