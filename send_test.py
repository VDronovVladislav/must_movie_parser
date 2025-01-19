import requests
from bs4 import BeautifulSoup
import re
#from constants import CEST_HEADERS


# def send_request():
#     #for id, rate in movies_list:
#     data = {
#         "status": "watched",
#         "rate": 8,
#         "review": {
#             "body": None
#         }
#     }
#     url = f'https://mustapp.com/api/users/id/846391/products/324'
#     response = requests.patch(url, json=data, headers=CEST_HEADERS)
#     print(response.status_code)

#send_request()

response = requests.get('https://mustapp.com/@ilyas_potash').text
# user_id = re.split(r'"user_id":|,"product_id"', response)[1]
# print(user_id)
match = re.search(r'"user_id":(\d+)', response)
if match:
    user_id = match.group(1)
    print(user_id)
