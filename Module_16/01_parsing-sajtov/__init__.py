from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import datetime
import csv


def write_cmc_top():
    # Создание драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Парсинг сайта
    url = 'https://coinmarketcap.com/ru/'
    driver.get(url)
    driver.execute_script("setInterval(function(){window.scrollBy({ top: 512, behavior: 'smooth' });}, 300)")
    time.sleep(10)

    # Создание необходимых коллекций для дальнейшей записи в файл
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    list_of_name, list_of_mc = [], []
    for coin in soup.find_all('tr')[1:]:
        list_of_name.append((coin.find_next('p', class_='sc-71024e3e-0 ehyBa-d').get_text().replace(' ', '_')))
        list_of_mc.append(coin.find_next('span', class_='sc-11478e5d-1 hwOFkt').get_text()[1:])
    capitalization_of_top_100 = sum(map(lambda x: int(x.replace(',', '')), list_of_mc))
    list_of_mp = [100 / capitalization_of_top_100 * mc for mc in map(lambda x: int(x.replace(',', '')), list_of_mc)]

    # Запись данных в файл
    with open(f'{datetime.datetime.now().strftime('%H.%M %d.%m.%Y')}.csv', 'w', encoding='utf-8') as output:
        csv_out = csv.writer(output, delimiter=' ', lineterminator="\r")
        csv_out.writerow(['Name', 'MC(RUB)', 'MP'])
        cnt = 0
        for name, mc, mp in zip(list_of_name, list_of_mc, list_of_mp):
            csv_out.writerow([name, mc, f'{round(mp, 2)}%'])
            cnt += 1

    # Успех!
    print(f'Файл {output.name} записан! Кол-во строк {cnt}')


if __name__ == "__main__":
    write_cmc_top()
