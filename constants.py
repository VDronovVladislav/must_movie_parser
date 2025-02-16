import os
from dotenv import load_dotenv

load_dotenv(override=True)


MUST_TOKEN = os.getenv('MUST_TOKEN')
USER_ID = os.getenv('USER_ID')
USER_TO_PARSE = os.getenv('USER_TO_PARSE')
USERS_NAMES = os.getenv('USERS_NAMES').split(',')

MAIN_URL = 'https://mustapp.com'
PRODUCT_SUFFIX = 'products?embed=product'
REVIEW_SUFFIX = 'products?embed=review'
SHOWS_SUFFIX = 'shows/watched_stats'
MOVIE_PREFIX_PATH = 'https://media.mustapp.me/must/posters/w342'

HEADERS = {
    "bearer": MUST_TOKEN,
    "content-type": "application/json;v=1873",
    "accept-Language": "ru"
}
