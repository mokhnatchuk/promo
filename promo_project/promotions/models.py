from django.db import models

class Promotion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
