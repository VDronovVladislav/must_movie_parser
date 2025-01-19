from configs import configure_argument_parser
from utils import (
    parse_data, prepare_hrefs, prepare_movies_data, prepare_series_data, prepare_want_data,
    prepare_db_data, get_engine, create_db, send_want_request, send_watched_request, 
)
from constants import MAIN_URL, USER_TO_PARSE, URLS_LIST


def must_want():
    """Парсинг и добавление в базу фильмов в раздел 'Посмотрю'."""
    url = f'{MAIN_URL}/{USER_TO_PARSE}/want'
    parsed_data = parse_data(url)
    prepared_data = prepare_want_data(parsed_data)
    print(len(prepared_data))
    print(prepared_data[0])
    send_want_request(prepared_data)


def must_watched():
    """Парсинг и добавление в базу фильмов и оценок в раздел 'Просмотрены'."""
    url = f'{MAIN_URL}/{USER_TO_PARSE}/watched'
    parsed_data = parse_data(url)
    prepared_data = prepare_movies_data(parsed_data)
    send_watched_request(prepared_data)


def must_shows():
    """Парсинг и добавление в базу сериалов и оценок в раздел 'Сериалы'."""
    url = f'{MAIN_URL}/{USER_TO_PARSE}/shows'
    parsed_data = parse_data(url)
    prepared_hrefs = prepare_hrefs(parsed_data)
    prepared_data = prepare_series_data(prepared_hrefs)
    send_watched_request(prepared_data)


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