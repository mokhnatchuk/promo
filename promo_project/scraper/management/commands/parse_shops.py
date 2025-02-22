from django.core.management.base import BaseCommand
from scraper.parsers import parse_shop  # Імпортуємо функцію для парсингу

# Цей код створює команду Django для запуску парсингу безпосередньо з командного 
# рядка. Це зручний спосіб для запуску парсингу з адміністраторської консолі 
# або через певний cron-робітник, що дозволяє автоматизувати процес збору даних 
# без необхідності запускати окремий скрипт вручну.

class Command(BaseCommand):
    help = 'Парсить сайти магазинів'

    def handle(self, *args, **kwargs):
        parse_shop()  # Викликаємо функцію парсингу
        self.stdout.write(self.style.SUCCESS('Парсинг завершено'))

