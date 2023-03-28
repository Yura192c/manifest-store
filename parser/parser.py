import requests
from bs4 import BeautifulSoup
from translate import Translator
import time
import os
# from fake_useragent import UserAgent
from parser.config import ua

translator = Translator(to_lang="ru")
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'User-Agent': ua.random
}


def update_price_NB(url_to_parse):
    product_data = {}
    response = requests.get(url_to_parse, headers=headers)
    if response.status_code == 200:
        pass

    soup = BeautifulSoup(response.text, 'lxml')
    price = float(soup.find('div', class_='col-lg-12 col-12 p-0 d-none d-lg-block mb-2') \
                  .find_all('div', class_='row')[2] \
                  .find('div', class_='col') \
                  .find('div', class_='prices pb-0') \
                  .find('div', class_='price') \
                  .find('span', class_='price-value') \
                  .find('span').get_text().translate({ord(i): None for i in '\n'}).replace('$', ''))
    return price


def parse_NB(url_to_parse):
    product_data = {}
    response = requests.get(url_to_parse, headers=headers)
    if response.status_code == 200:
        pass

    soup = BeautifulSoup(response.text, 'lxml')
    product_data['name'] = soup.find('div', class_='col-lg-12 col-12 p-0 d-none d-lg-block mb-2') \
        .find_all('div', class_='row')[1] \
        .find('div', class_='col') \
        .find('h1').get_text()

    product_data['price'] = float(soup.find('div', class_='col-lg-12 col-12 p-0 d-none d-lg-block mb-2') \
                                  .find_all('div', class_='row')[2] \
                                  .find('div', class_='col') \
                                  .find('div', class_='prices pb-0') \
                                  .find('div', class_='price') \
                                  .find('span', class_='price-value') \
                                  .find('span').get_text().translate({ord(i): None for i in '\n'}).replace('$', ''))
    descroption = soup.find('div', class_='col-12 value content short-description px-0 pt-6 pt-lg-4 pb-3') \
        .get_text().translate({ord(i): None for i in '\n'}).replace('Description', '')
    product_data['description'] = translator.translate(descroption)

    sizes = soup.find_all('div', class_='row dyanamic-attr')[0].find_all('button')
    size = []
    for s in sizes:
        size.append(s.find('span', class_='sr-only selected-assistive-text').get('id'))

    product_data['sizes'] = size

    images = []
    image = soup.find('div', class_='carousel-inner carousel-desktop').find_all('div', class_='carousel-item')
    for i in image:
        try:
            img_src = i.find('img').get('data-src')
            images.append(img_src)
        except:
            pass
    product_data['images'] = images
    return product_data