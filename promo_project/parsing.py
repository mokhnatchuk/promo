import json
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

# Налаштування Selenium
options = uc.ChromeOptions()
options.headless = False  # Відкрити браузер для перевірки
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

# Масив для збереження товарів
products_list = []

# Запуск браузера
with uc.Chrome(options=options) as driver:
    url = 'https://www.atbmarket.com/catalog/cipsi'
    driver.get(url)
    
    # Чекаємо завантаження сторінки
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/section/div/div/div[1]/div[2]/div[2]/div[2]/article[1]"))
        )
        print(f"Сторінка завантажена: {url}")
        
        time.sleep(5)  # Додатковий час для підвантаження товарів
        
        # Отримуємо блок товарів, а не весь HTML
        product_section = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div[1]/div[2]/div[2]/div[2]")
        product_html = product_section.get_attribute("outerHTML")
        
        with open("atb_page.html", "w", encoding="utf-8") as f:
            f.write(product_html)
        print("Збережено тільки HTML блоку товарів у atb_page.html")
        
        products = driver.find_elements(By.XPATH, "//*[@id='main']/section/div/div/div[1]/div[2]/div[2]/div[2]/article")
        
        if products:
            for i in range(len(products)):
                for attempt in range(3):  # Повторити до 3 разів
                    try:
                        # Оновлюємо список товарів перед кожною ітерацією
                        products = driver.find_elements(By.XPATH, "//*[@id='main']/section/div/div/div[1]/div[2]/div[2]/div[2]/article")
                        product = products[i]
                        
                        name_element = WebDriverWait(product, 5).until(
                            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/a"))
                        )
                        price_elements = product.find_elements(By.XPATH, ".//div[4]")
                        
                        name = name_element.text.strip()
                        
                        # Беремо тільки першу коректну ціну
                        price = "Ціна не знайдена"
                        for price_element in price_elements:
                            price_text = price_element.text.strip()
                            if "грн" in price_text:
                                price = price_text
                                break
                        
                        print(f"Знайдено товар: {name} - {price}")
                        
                        # Додаємо товар у список
                        products_list.append({"name": name, "price": price})
                        break  # Вийти з циклу повторних спроб, якщо успішно
                    except Exception as e:
                        print(f"Помилка при обробці товару, повторюємо спробу: {e}")
                        time.sleep(2)
        else:
            print("Товари не знайдені, оновлюємо сторінку...")
            driver.refresh()
            time.sleep(5)  # Дати час на оновлення
            
    except Exception as e:
        print(f"Помилка: {e}")

# Збереження в JSON
with open("results.json", "w", encoding="utf-8") as json_file:
    json.dump(products_list, json_file, ensure_ascii=False, indent=4)
print("✅ Дані збережено в results.json")

# Збереження в CSV
with open("results.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["name", "price"])
    writer.writeheader()
    writer.writerows(products_list)
print("✅ Дані збережено в results.csv")
