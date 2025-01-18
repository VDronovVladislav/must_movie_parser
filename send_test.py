import requests
from constants import CEST_HEADERS


def send_request():
    #for id, rate in movies_list:
    data = {
        "status": "watched",
        "rate": 8,
        "review": {
            "body": None
        }
    }
    url = f'https://mustapp.com/api/users/id/846391/products/324'
    response = requests.patch(url, json=data, headers=CEST_HEADERS)
    print(response.status_code)

send_request()