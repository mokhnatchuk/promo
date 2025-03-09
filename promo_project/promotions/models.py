from django.db import models

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'
