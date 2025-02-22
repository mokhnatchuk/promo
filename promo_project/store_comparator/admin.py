from django.contrib import admin
from .models import Store, Product, Price # Зв'язуємось з models.py

# Цей код дозволяє керувати даними через вбудований інтерфейс Django.

# Реєструємо моделі в адмінці
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Price)