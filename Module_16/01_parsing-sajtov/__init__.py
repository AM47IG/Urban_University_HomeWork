from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
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
    driver.execute_script("setInterval(function(){window.scrollBy({ top: 1024 });}, 500)")
    time.sleep(7)

    assert driver.current_url == 'https://coinmarketcap.com/ru/'
    soup = BeautifulSoup(driver.page_source, features='html.parser')

    # Создание необходимых коллекций для дальнейшей записи в файл
    list_of_name, list_of_mc = [], []
    for coin in soup.find_all('tr')[1:]:
        list_of_name.append((coin.find_next('p', class_='sc-71024e3e-0 ehyBa-d').get_text().replace(' ', '_')))
        list_of_mc.append(coin.find_next('span', class_='sc-11478e5d-1 hwOFkt').get_text()[1:])
    capitalization_of_top_100 = sum(map(lambda x: int(x.replace(',', '')), list_of_mc))
    list_of_mp = [100 / capitalization_of_top_100 * mc for mc in map(lambda x: int(x.replace(',', '')), list_of_mc)]

    assert len(set(list_of_name)) == 100 and len(list_of_name) == 100, \
        f'Ошибка! Считано {len(set(list_of_name))} строк вместо 100.'

    # Запись данных в файл
    with open(f'{datetime.datetime.now().strftime('%H.%M %d.%m.%Y')}.csv', 'w', encoding='utf-8') as output:
        csv_out = csv.writer(output, delimiter=' ', lineterminator="\r")
        csv_out.writerow(['Name', 'MC(RUB)', 'MP'])
        for name, mc, mp in zip(list_of_name, list_of_mc, list_of_mp):
            csv_out.writerow([name, mc, f'{round(mp, 2)}%'])

    # Успех!
    print(f'Файл {output.name} записан!')


if __name__ == "__main__":
    write_cmc_top()
