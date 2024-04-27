from urllib.parse import urljoin

MAIN_URL = 'https://mustapp.com/'

VLAD_URL = '@Selave/watched'
TEMA_URL = '@Pactasuntservanda/watched'
ILYA_URL = '@ilyas_potash/watched'

vlad_url = urljoin(MAIN_URL, VLAD_URL)
tema_url = urljoin(MAIN_URL, TEMA_URL)
ilya_url = urljoin(MAIN_URL, ILYA_URL)

URL_LIST = [vlad_url, tema_url, ilya_url]
