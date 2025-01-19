import time
import requests

from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm

from constants import REVIEW_SUFFIX, USER_URL, SHOWS_SUFFIX


def create_data_list(url, data_list):
    """Функция получения списка с данными для дальнейшего добавления."""
    left = 0
    right = 100
    list_to_response = []
    while left < len(data_list):
        data = {
            "ids": data_list[left:right]
        }
        response = requests.post(url, json=data).json()
        if 'watched_seasons' in response[0].keys():
            for elem in response:
                seasons = elem['watched_seasons']
                for season in seasons:
                    list_to_response.append(season)
        elif 'user_product_info' in response[0].keys():
            for elem in response:
                movie_id = elem['user_product_info']['product_id']
                rate = elem['user_product_info']['rate']
                list_to_response.append((movie_id, rate))
        left += 100
        right += 100
    return list_to_response


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
    print(len(shows_list))
    stats_url = f'{url}/{SHOWS_SUFFIX}'
    watched_seasons = create_data_list(stats_url, shows_list) 
    info = f'{url}/{REVIEW_SUFFIX}'
    series_list = create_data_list(info, watched_seasons)
    print(series_list)
    return series_list



#print(get_want_data(USER_URL))
#print(get_watched_data(USER_URL))
#print(get_shows_data(USER_URL))
#create_watched_data(USER_URL)

create_shows_data(USER_URL)


