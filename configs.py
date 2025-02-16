import argparse


def configure_argument_parser(available_modes):
    """Функция-конфигуратор парсера."""
    parser = argparse.ArgumentParser(description='Парсер Must')
    parser.add_argument('mode', choices=available_modes, help='Режимы работы парсера')
    parser.add_argument(
        '-r', '--rating',
        help=('При создании базы с фильмами. '
              'Режим must_db_create - добавляет фильтмы только от указанного рейтинга и выше'),
        type=int
    )
    return parser