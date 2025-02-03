from configs import configure_argument_parser
from utils import (
    get_engine, get_user_id_to_parse, get_user_url, create_want_data, create_watched_data,
    create_shows_data, create_db_data, create_db, send_watched_request, send_want_request
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
    print(want_list)
    print(len(want_list))
    #send_want_request(want_list)


def must_watched():
    """Парсинг и добавление в базу фильмов и оценок в раздел 'Просмотрены'."""
    watched_list = main_parser(create_watched_data)
    print(watched_list)
    print(len(watched_list))
    #send_watched_request(watched_list)


def must_shows():
    """Парсинг и добавление в базу сериалов и оценок в раздел 'Сериалы'."""
    shows_list = main_parser(create_shows_data)
    print(shows_list)
    print(len(shows_list))
    #send_watched_request(prepared_data)


def must_db_create():
    """Создание базы данных из просмотренных фильмов."""
    engine = get_engine()
    overlap = set()
    for user_to_parse in USERS_NAMES:
        user_id = get_user_id_to_parse(user_to_parse)
        url = get_user_url(user_id)
        movies_set = set(create_db_data(url))
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
    MODE_TO_FUNCTION[parser_mode]()


if __name__ == '__main__':
    main()

# TODO:
# 1: Переписать код для асинхронной отправки запросов на добавление
# 2: Протестировать все с новым пользователем
# 3: Логирование + обработка ошибок (возможно)
# 4: Почистить существующие файлы + удалить лишние.