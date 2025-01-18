import argparse


def configure_argument_parser(available_modes):
    """Функция-конфигуратор парсера."""
    parser = argparse.ArgumentParser(description='Парсер Must')
    parser.add_argument('mode', choices=available_modes, help='Режимы работы парсера')
    # parser.add_argument(
    #     'name', help='Никнейм пользователя Must, базу которого нужно спарсить в формате @Username'
    # )
    return parser