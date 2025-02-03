import requests
import re

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from constants import (
    MAIN_URL, HEADERS, REVIEW_SUFFIX, SHOWS_SUFFIX, PRODUCT_SUFFIX, USER_ID, MOVIE_PREFIX_PATH
)
from models import Base, Movie


def get_engine():
    """Функция получения соединения с базой."""
    engine = create_engine(f'sqlite:///sqlite3.db')
    Base.metadata.create_all(engine)
    return engine


def get_user_id_to_parse(username):
    """Функция получения id пользователя, чьи данные нужно спарсить."""
    url = f'{MAIN_URL}/{username}'
    response = requests.get(url).text
    match = re.search(r'"user_id":(\d+)', response)
    user_id = match.group(1)
    return user_id


def get_user_url(user_id):
    """Функция подготовки user_url - пользователя, чьи данные парсим."""
    return f'{MAIN_URL}/api/users/id/{user_id}'


def get_api_url():
    """Функция получения api_url - пользоветеля, для которого добавляем данные."""
    return f'{MAIN_URL}/api/users/id/{USER_ID}/products'


def create_data_list(url, ids_list):
    """Функция получения списка с данными для дальнейшего добавления/создания БД."""
    left = 0
    right = 100
    data_list = []
    while left < len(ids_list):
        data = {
            "ids": ids_list[left:right]
        }
        response = requests.post(url, json=data, headers={"accept-Language": "ru"}).json()
        if 'watched_seasons' in response[0].keys():
            for elem in response:
                seasons = elem['watched_seasons']
                for season in seasons:
                    data_list.append(season)
        elif 'product' in response[0].keys():
            for elem in response:
                movie_title = elem['product']['title']
                movie_href = MOVIE_PREFIX_PATH + elem['product']['poster_file_path']
                data_list.append((movie_title, movie_href))                    
        elif 'user_product_info' in response[0].keys():
            for elem in response:
                movie_id = elem['user_product_info']['product_id']
                rate = elem['user_product_info']['rate']
                data_list.append((movie_id, rate))
        left += 100
        right += 100
    return data_list


def create_want_data(url):
    """Функция подготовки списка с id фильмов (API)."""
    response = requests.get(url).json()
    want_list = response['lists']['want']
    return want_list


def create_watched_data(url):
    """Функция подготовки списка с id и рейтингами фильмов (API)."""
    response = requests.get(url).json()
    watched_list = response['lists']['watched']
    info_url = f'{url}/{REVIEW_SUFFIX}'
    movies_list = create_data_list(info_url, watched_list)
    return movies_list


def create_shows_data(url):
    """Функция подготовки списка с id и рейтингами сезонов сериалов (API)."""
    response = requests.get(url).json()
    shows_list = response['lists']['shows']
    stats_url = f'{url}/{SHOWS_SUFFIX}'
    watched_seasons = create_data_list(stats_url, shows_list) 
    info_url = f'{url}/{REVIEW_SUFFIX}'
    series_list = create_data_list(info_url, watched_seasons)
    return series_list


def create_db_data(url):
    """Функция подготовки списка с названием и ссылкой на постер фильма для создания БД (API)."""
    response = requests.get(url).json()
    watched_list = response['lists']['watched']
    info_url = f'{url}/{PRODUCT_SUFFIX}'
    db_movies_list = create_data_list(info_url, watched_list)
    return db_movies_list


def create_db(overlap, engine):
    """Функция создания базы данных с фильмами."""
    with Session(engine) as db_session:
        db_session.execute(
            insert(Movie), [{"name": movie[0], "image": movie[1]} for movie in overlap]
        )
        db_session.commit()


def send_watched_request(data_list):
    """Функция отправки запросов на добавление фильмов/сериалов в просмотренные."""
    for id, rate in data_list:
        data = {
            "status": "watched",
            "rate": rate,
            "review": {
                "body": None
            }
        }
        url_prefix = get_api_url()
        url = f'{url_prefix}/{id}'
        response = requests.patch(url, json=data, headers=HEADERS)
        print(response.status_code)


def send_want_request(data_list):
    """Функция отправки запросов на добавление фильмов в посмотрю."""
    for id in data_list:
        data = {
            "status": "want",
        }
        url_prefix = get_api_url()
        url = f'{url_prefix}/{id}'
        response = requests.patch(url, json=data, headers=HEADERS)
        print(response.status_code)