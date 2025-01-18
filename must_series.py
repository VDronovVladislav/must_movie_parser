import time
import requests

from selenium import webdriver
from bs4 import BeautifulSoup

from constants import vlad_new_url, CEST_HEADERS, vlad_url, MAIN_URL, selave_series_url, HREF_LIST, SERIES_DATA


def parse_data(url):
    """Функция парсинга данных страницы."""
    driver = webdriver.Chrome()
    driver.get(url)
    last_height = driver.execute_script(
        "return document.body.scrollHeight"
    )
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        #time.sleep(5)
        new_height = driver.execute_script(
            "return document.body.scrollHeight"
        )
        if new_height == last_height:
            break
        last_height = new_height
    html = driver.page_source
    driver.quit()
    print('Функция parse_data закончила работу')
    return html


def prepare_hrefs(html):
    """Функция подготовки списка с cсылками на сериалы."""
    soup = BeautifulSoup(html, 'html.parser')
    content_a = soup.find_all('a', class_='poster js_item js_item_product')
    href_list = []
    for elem in content_a:
        href = MAIN_URL + elem['href']
        href_list.append(href)
    print(len(href_list))
    print(href_list)
    return href_list


def prepare_data(href_list):
    series_list = []
    for href in href_list:
        html = parse_data(href)
        soup = BeautifulSoup(html, 'html.parser')
        content_div_active = soup.find('div', class_='profileProduct__season js_season m_active')
        try:
            rate = content_div_active.find('div', class_='poster__rate_stars').text
        except AttributeError:
            rate = None
        series_list.append((content_div_active['data-season'], rate))
        # content_div = soup.find_all('div', class_='profileProduct__season js_season')
        # for elem in content_div:
        #     id = elem['data-season']
        #     try:
        #         rate = elem.find('div', class_='poster__rate_stars').text
        #     except AttributeError:
        #         rate = None
        #     series_list.append((id, rate))
    print(series_list)
    return series_list


def send_request(series_list):
    for id, rate in series_list:
        data = {
            "status": "watched",
            "rate": int(rate) if rate else None,
            "review": {
                "body": None
            }
        }
        url = f'https://mustapp.com/api/users/id/846391/products/{id}'
        response = requests.patch(url, json=data, headers=CEST_HEADERS)
        print(response.status_code)


#parsed_data = parse_data(selave_series_url)
#prepared_hrefs = prepare_hrefs(parsed_data)
#print(prepared_hrefs)
prepared_data = prepare_data(HREF_LIST)
#print(prepared_data)
send_request(prepared_data)

# html = parse_data('https://mustapp.com/@Selave/1341454')
# soup = BeautifulSoup(html, features='html.parser')
# content_div = soup.find('div', class_='profileProduct__season js_season m_active')
# print(content_div['data-season'])

