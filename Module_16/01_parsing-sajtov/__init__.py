from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import csv


def write_cmc_top():
    # Создание и конфигурация драйвера
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # options.add_argument('--blink-settings=imagesEnabled=false')  # Нестабильная загрузка с этим параметром!
    options.page_load_strategy = ('none', 'eager', 'normal')[1]
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as exc:
        print(f'Ошибка {exc.args}. Пробуем обновить драйвер!')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Парсинг сайта
    url = 'https://coinmarketcap.com/ru/'
    driver.get(url)
    driver.execute_script("setInterval(function(){window.scrollBy({ top: 1024, behavior: 'smooth' });}, 500)")
    time.sleep(7)
    assert driver.current_url == 'https://coinmarketcap.com/ru/', 'Некорректный URL!'

    # Создание необходимых коллекций для дальнейшей записи в файл
    list_of_names = driver.find_elements("xpath", "//table//p[@class = 'sc-71024e3e-0 ehyBa-d']")
    list_of_mc = driver.find_elements("xpath", "//table//span[@class = 'sc-11478e5d-1 jfwGHx']")
    assert len(set(list_of_names)) == 100 and len(list_of_names) == 100, f'Считано не 100 строк!'

    list_of_names = [web_element.text.replace(' ', '_') for web_element in list_of_names]
    list_of_mc = [int(web_element.text[1:].replace(',', '')) for web_element in list_of_mc]
    list_of_mp = [100 / sum(list_of_mc) * mc for mc in list_of_mc]

    # Запись данных в файл
    with open(f'{datetime.datetime.now():%H.%M %d.%m.%Y}.csv', 'w', encoding='utf-8') as output:
        csv_out = csv.writer(output, delimiter=' ', lineterminator="\r")
        csv_out.writerow(['Name', 'MC(RUB)', 'MP'])
        for name, mc, mp in zip(list_of_names, list_of_mc, list_of_mp):
            csv_out.writerow([name, f'{mc:,}', f'{mp:.2f}%'])

    # Успех!
    print(f'Файл {output.name} записан!')


if __name__ == "__main__":
    write_cmc_top()
