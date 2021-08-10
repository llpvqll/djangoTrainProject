
import requests
from bs4 import BeautifulSoup
import csv

URL = input('Entry URL: ')

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='proposition')
    cars = []
    for item in items:
        uah_price = item.find('span', class_='size16')
        if uah_price:
            uah_price = uah_price.get_text()
        else:
            uah_price = 'Вточнюйте ціну'
        cars.append({
            'title': item.find('span', class_='link').get_text(strip=True),
            'link': HOST + item.find('a', class_='proposition_link').get('href'),
            'usd_price': item.find('span', class_='green').get_text(strip=True),
            'uah_price': uah_price,
            'city': item.find('span', class_='region').get_text(strip=True)
        })
    return cars


def save_file(items):
    with open('cars.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='; ')
        writer.writerow(['Mark', 'URL', 'Price in $', 'Price in UAH', 'City'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_price'], item['uah_price'], item['city']])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count+1):
            print(f'Парсинг сторінки {page} з {pages_count}...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        print(cars)
        save_file(cars)
        print(f'Отримано {len(cars)} автомобілей')
    else:
        print("Error")


parse()
