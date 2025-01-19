from configs import configure_argument_parser
from utils import (
    parse_data, prepare_db_data, get_engine, create_db, get_user_url, get_user_id_to_parse, 
    create_want_data, create_watched_data, create_shows_data, send_want_request, 
    send_watched_request
)
from constants import USER_TO_PARSE, URLS_LIST


def must_want():
    """Парсинг и добавление в базу фильмов в раздел 'Посмотрю'."""
    user_id = get_user_id_to_parse(USER_TO_PARSE)
    url = get_user_url(user_id)
    want_list = create_want_data(url)
    send_want_request(want_list)


def must_watched():
    """Парсинг и добавление в базу фильмов и оценок в раздел 'Просмотрены'."""
    user_id = get_user_id_to_parse(USER_TO_PARSE)
    url = get_user_url(user_id)
    watched_list = create_watched_data(url)
    #send_watched_request(watched_list)


def must_shows():
    """Парсинг и добавление в базу сериалов и оценок в раздел 'Сериалы'."""
    user_id = get_user_id_to_parse(USER_TO_PARSE)
    url = get_user_url(user_id)
    shows_list = create_shows_data(url)
    #send_watched_request(prepared_data)


def must_db_create():
    """Создание базы данных из просмотренных фильмов."""
    engine = get_engine()
    overlap = set()
    for url in URLS_LIST:
        html = parse_data(url)
        movies_set = set(prepare_db_data(html))
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