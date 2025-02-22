from django.db import models

# Цей код дозволяє зберігати структуру даних про магазини, продукти та ціни в базі даних.

class Store(models.Model):
    """Клас який відповідає за зберігання інформації про кожен магазин у базі даних."""
    name = models.CharField(max_length=100) # назви магазину 
    address = models.CharField(max_length=255) # поле для зберігання адреси магазину

class Product(models.Model):
    """Клас який зберігає інформацію про самі продукти."""
    name = models.CharField(max_length=100) # назви продукту
    category = models.CharField(max_length=100) # назви категорій

class Price(models.Model):
    """Клас який зберігає ціни та знижки (у відсотках) на продукти"""
    store = models.ForeignKey(Store, on_delete=models.CASCADE) # зв'язок з моделлю Store
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # зв'язок з моделлю Product
    price = models.DecimalField(max_digits=10, decimal_places=2) # це поле для зберігання ціни продукту в магазині
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0) # це поле для зберігання знижки на товар (у відсотках)

# Ми використовуємо ForeignKey для зв'язку "багато до одного".


# Я налаштуємо сервер треба буде зробити міграції:
# python manage.py makemigrations
# python manage.py migrate