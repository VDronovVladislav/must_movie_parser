import time
import requests

from selenium import webdriver
from bs4 import BeautifulSoup

from constants import vlad_new_url, CEST_HEADERS, vlad_url, will_watch_url


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
        time.sleep(3)
        new_height = driver.execute_script(
            "return document.body.scrollHeight"
        )
        if new_height == last_height:
            break
        last_height = new_height
    html = driver.page_source
    driver.quit()
    return html


def prepare_data(html):
    """Функция подготовки списка с заголовками и рейтингами фильмов."""
    soup = BeautifulSoup(html, 'html.parser')
    content_a = soup.find_all('a', class_='poster js_item')
    movies_list = []
    for elem in content_a:
        id = elem['data-product']
        movies_list.append(id)
    return movies_list


def send_request(movies_list):
    for id in movies_list:
        data = {
            "status": "want",
        }
        url = f'https://mustapp.com/api/users/id/846391/products/{id}'
        response = requests.patch(url, json=data, headers=CEST_HEADERS)
        print(response.status_code)

parsed_data = parse_data(will_watch_url)
prepared_date = prepare_data(parsed_data)
send_request(prepared_date)


