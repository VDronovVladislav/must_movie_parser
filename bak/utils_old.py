import time
import requests
from urllib.parse import urljoin

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from selenium import webdriver
from bs4 import BeautifulSoup

from constants import MAIN_URL, HEADERS, API_URL
from models import Base, Movie


def get_engine():
    engine = create_engine(f'sqlite:///sqlite3.db')
    Base.metadata.create_all(engine)
    return engine


def parse_data(url):
    """Функция парсинга данных страницы."""
    driver = webdriver.Chrome()
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    html = driver.page_source
    driver.quit()
    return html


def prepare_hrefs(html):
    """Функция подготовки списка с cсылками на сериалы."""
    soup = BeautifulSoup(html, 'html.parser')
    content_a = soup.find_all('a', class_='poster js_item js_item_product')
    href_list = []
    for elem in content_a:
        href = urljoin(MAIN_URL, elem['href'])
        href_list.append(href)
    return href_list


def prepare_movies_data(html):
    """Функция подготовки списка с id и рейтингами фильмов (парсинг HTML)."""
    soup = BeautifulSoup(html, 'html.parser')
    content_a = soup.find_all('a', class_='poster js_item js_item_product')
    movies_list = []
    for elem in content_a:
        id = elem['data-product']
        try:
            rate = elem.find('div', class_='poster__rate_stars').text
        except AttributeError:
            rate = None
        movies_list.append((id, rate))
    return movies_list


def prepare_want_data(html):
    """Функция подготовки списка с id фильмов (парсинг HTML)."""
    soup = BeautifulSoup(html, 'html.parser')
    content_a = soup.find_all('a', class_='poster js_item')
    movies_list = []
    for elem in content_a:
        id = elem['data-product']
        movies_list.append(id)
    return movies_list


def prepare_series_data(href_list):
    """Функция подготовки списка с id и рейтингами сезонов сериалов (парсинг HTML)."""
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
        content_div = soup.find_all('div', class_='profileProduct__season js_season')
        for elem in content_div:
            id = elem['data-season']
            try:
                rate = elem.find('div', class_='poster__rate_stars').text
            except AttributeError:
                rate = None
            series_list.append((id, rate))
    return series_list


def prepare_db_data(html):
    """Функция подготовки списка с названием фильма и ссылкой на постер (парсинг HTML)."""
    movies_list = []
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', class_='profile__list_content js_items')
    poster_titles = content_div.find_all('div', class_='poster__title')
    poster_arts = content_div.find_all('div', class_='poster__art')

    for poster_title, poster_art in zip(poster_titles, poster_arts):
        title = poster_title.text
        href = poster_art['style'].split('"')[1]
        movies_list.append((title, href))
    return movies_list


def create_db(overlap, engine):
    """Функция создания базы данных с фильмами."""
    for movie in overlap:
        db_session = Session(engine)
        db_session.execute(
            insert(Movie).values(
                name=movie[0],
                image=movie[1]
            )
        )
        db_session.commit()


def send_watched_request(data_list):
    """Функция отправки запросов на добавление фильмов/сериалов в просмотренные."""
    for id, rate in data_list:
        data = {
            "status": "watched",
            "rate": int(rate) if rate else rate,
            "review": {
                "body": None
            }
        }
        url = f'{API_URL}/{id}'
        response = requests.patch(url, json=data, headers=HEADERS)
        print(response.status_code)


def send_want_request(data_list):
    """Функция отправки запросов на добавление фильмов в посмотрю."""
    for id in data_list:
        data = {
            "status": "want",
        }
        url = f'{API_URL}/{id}'
        response = requests.patch(url, json=data, headers=HEADERS)
        print(response.status_code)    