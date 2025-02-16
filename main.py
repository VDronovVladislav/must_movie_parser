import asyncio

from configs import configure_argument_parser
from utils import (
    get_engine, get_user_id_to_parse, get_user_url, create_want_data, create_watched_data,
    create_shows_data, create_db_data, create_db, async_execute
)
from constants import USER_TO_PARSE, USERS_NAMES


def main_parser(create_data_func):
    """Базовая функция для получения данных."""
    user_id = get_user_id_to_parse(USER_TO_PARSE)
    url = get_user_url(user_id)
    data_list = create_data_func(url)
    return data_list


def must_want():
    """Парсинг и добавление в базу фильмов в раздел 'Посмотрю'."""
    want_list = main_parser(create_want_data)
    asyncio.run(async_execute(want_list, 'want'))


def must_watched():
    """Парсинг и добавление в базу фильмов и оценок в раздел 'Просмотрены'."""
    watched_list = main_parser(create_watched_data)
    asyncio.run(async_execute(watched_list, 'watched'))


def must_shows():
    """Парсинг и добавление в базу сериалов и оценок в раздел 'Сериалы'."""
    shows_list = main_parser(create_shows_data)
    asyncio.run(async_execute(shows_list, 'watched'))


def must_db_create(rating=None):
    """Создание базы данных из просмотренных фильмов."""
    engine = get_engine()
    overlap = set()
    for user_to_parse in USERS_NAMES:
        user_id = get_user_id_to_parse(user_to_parse)
        url = get_user_url(user_id)
        movies_set = set(create_db_data(url, rating))
        if overlap:
            overlap = overlap & movies_set
        else:
            overlap = movies_set
    create_db(overlap, engine)


MODE_TO_FUNCTION = {
    'must_want': must_want,
    'must_watched': must_watched,
    'must_shows': must_shows,
    'must_db_create': must_db_create
}


def main():
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    parser_mode = args.mode

    if parser_mode == 'must_db_create':
        rating = args.rating
        MODE_TO_FUNCTION[parser_mode](rating)
    else:
        MODE_TO_FUNCTION[parser_mode]()


if __name__ == '__main__':
    main()