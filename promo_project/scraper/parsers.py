import requests
from bs4 import BeautifulSoup
# підключаємось до models.py
from store_comparator.models import Store, Product, Price

# Список магазинів та їх посилань на акційні сторіки
url_shops = {
    'atb': 'https://www.atbmarket.com/promo/economy',
    'silpo': 'https://silpo.ua/offers',
    'sim23': 'https://sim23.ua/promo/',
    'METRO': 'https://shop.metro.ua/shop/storelist/ba9ac72f-05af-471e-9a9e-11a3bb9cc985',
}

# Функція для отримання даних з сторінки
def parse_shop(shop_name, url):
    # Використовуємо requests для отримання сторінки
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Приклад: знаходимо всі товари на сторінці (можна змінити в залежності від сайту)
        products = soup.find_all('div', class_='product-item')

        for product in products:
            name = product.find('h3').text.strip() if product.find('h3') else 'Unknown product'
            price = product.find('span', class_='price').text.strip() if product.find('span', class_='price') else '0'
            discount = product.find('span', class_='discount').text.strip() if product.find('span', class_='discount') else '0'

            # Створюємо або знаходимо продукт у базі даних
            product_obj, created = Product.objects.get_or_create(name=name)

            # Знаходимо магазин по його назві
            store, created = Store.objects.get_or_create(name=shop_name)

            # Створюємо нову ціну для продукту
            Price.objects.create(store=store, product=product_obj, price=price, discount=discount)

# Викликаємо функцію для кожного магазину
def parse_all_shops():
    for shop_name, url in url_shops.items():
        parse_shop(shop_name, url)


# Було додатково встановленні бібліотеки
# pip install requests beautifulsoup4
# pip install selenium