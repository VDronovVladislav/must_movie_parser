import os
from urllib.parse import urljoin
from dotenv import load_dotenv

load_dotenv()


MUST_TOKEN = os.getenv('MUST_TOKEN')
USER_ID = os.getenv('USER_ID')
USER_TO_PARSE = os.getenv('USER_TO_PARSE')
USERS_NAMES = os.getenv('USERS_NAMES').split(',')

MAIN_URL = 'https://mustapp.com'
API_URL = f'{MAIN_URL}/api/users/id/{USER_ID}/products'
URLS_LIST = [f"{MAIN_URL}/{user}/watched" for user in USERS_NAMES]

HEADERS = {
    "bearer": MUST_TOKEN,
    "content-type": "application/json;v=1873",
}



# VLAD_URL = '@Selave/watched'
# TEMA_URL = '@Pactasuntservanda/watched'
ILYA_URL = '@ilyas_potash/watched'

#vlad_url = f"{MAIN_URL}{VLAD_URL}"
# vlad_url = urljoin(MAIN_URL, VLAD_URL)
# tema_url = urljoin(MAIN_URL, TEMA_URL)
ilya_url = urljoin(MAIN_URL, ILYA_URL)

# vlad_new_url = 'https://mustapp.com/@Cestlavie/watched'

# selave_series_url = 'https://mustapp.com/@Selave/shows'

# will_watch_url = 'https://mustapp.com/@Selave/want'

# URL_LIST = [vlad_url, tema_url, ilya_url]
#
# db_name = ''

# for url in URL_LIST:
#     url_now = url.split('/')[3][1:]
#     db_name += url_now
#     if url != URL_LIST[-1]:
#         db_name += '-'


HREF_LIST = ['https://mustapp.com/@Selave/1341454', 'https://mustapp.com/@Selave/25905102', 'https://mustapp.com/@Selave/11799203', 'https://mustapp.com/@Selave/29311840', 'https://mustapp.com/@Selave/18936680', 'https://mustapp.com/@Selave/29254126', 'https://mustapp.com/@Selave/15396314', 'https://mustapp.com/@Selave/11916912', 'https://mustapp.com/@Selave/286009', 'https://mustapp.com/@Selave/20543070', 'https://mustapp.com/@Selave/22440994', 'https://mustapp.com/@Selave/23404748', 'https://mustapp.com/@Selave/10437656', 'https://mustapp.com/@Selave/288040', 'https://mustapp.com/@Selave/27226407', 'https://mustapp.com/@Selave/288540', 'https://mustapp.com/@Selave/13795586', 'https://mustapp.com/@Selave/9519651', 'https://mustapp.com/@Selave/288837', 'https://mustapp.com/@Selave/12886853', 'https://mustapp.com/@Selave/284119', 'https://mustapp.com/@Selave/284228', 'https://mustapp.com/@Selave/12187372', 'https://mustapp.com/@Selave/1238389', 'https://mustapp.com/@Selave/5289419', 'https://mustapp.com/@Selave/9946003', 'https://mustapp.com/@Selave/1801418', 'https://mustapp.com/@Selave/286244', 'https://mustapp.com/@Selave/285669', 'https://mustapp.com/@Selave/285677', 'https://mustapp.com/@Selave/347360', 'https://mustapp.com/@Selave/294373', 'https://mustapp.com/@Selave/299698', 'https://mustapp.com/@Selave/284132', 'https://mustapp.com/@Selave/305072', 'https://mustapp.com/@Selave/11448779', 'https://mustapp.com/@Selave/19562629', 'https://mustapp.com/@Selave/288014', 'https://mustapp.com/@Selave/22768923', 'https://mustapp.com/@Selave/15027987', 'https://mustapp.com/@Selave/29099333', 'https://mustapp.com/@Selave/284103', 'https://mustapp.com/@Selave/288597', 'https://mustapp.com/@Selave/286845', 'https://mustapp.com/@Selave/284222', 'https://mustapp.com/@Selave/287425', 'https://mustapp.com/@Selave/287065', 'https://mustapp.com/@Selave/17445996', 'https://mustapp.com/@Selave/285466', 'https://mustapp.com/@Selave/1331415', 'https://mustapp.com/@Selave/10883017', 'https://mustapp.com/@Selave/285631', 'https://mustapp.com/@Selave/2498270', 'https://mustapp.com/@Selave/291233', 'https://mustapp.com/@Selave/10043821', 'https://mustapp.com/@Selave/286176', 'https://mustapp.com/@Selave/827900', 'https://mustapp.com/@Selave/286463', 'https://mustapp.com/@Selave/285538', 'https://mustapp.com/@Selave/2302926', 'https://mustapp.com/@Selave/10019449', 'https://mustapp.com/@Selave/830945', 'https://mustapp.com/@Selave/10199696', 'https://mustapp.com/@Selave/6621333', 'https://mustapp.com/@Selave/285906', 'https://mustapp.com/@Selave/288717', 'https://mustapp.com/@Selave/289699', 'https://mustapp.com/@Selave/290010', 'https://mustapp.com/@Selave/287941', 'https://mustapp.com/@Selave/294597', 'https://mustapp.com/@Selave/298388', 'https://mustapp.com/@Selave/298986', 'https://mustapp.com/@Selave/286148']
SERIES_DATA = [('286011', '7'), ('7931671', '8'), ('25344402', '6'), ('26673393', '8'), ('19439974', '9'), ('288042', '10'), ('1399348', '10'), ('11074454', '10'), ('18594385', '10'), ('23623750', '10'), ('28904895', '10'), ('288542', '8'), ('288543', '8'), ('288544', '8'), ('288545', '8'), ('288546', '8'), ('288547', '8'), ('288548', '8'), ('288549', '8'), ('288550', '8'), ('8826694', '8'), ('21034677', '8'), ('288839', None), ('288840', None), ('4834418', None), ('10571805', '9'), ('21440787', '7'), ('507558', '7'), ('284919', '7'), ('284921', '7'), ('284922', '7'), ('507752', '5'), ('2434924', '7'), ('15047841', '9'), ('20549810', '9'), ('18596295', '9'), ('22409721', '9'), ('1682341', '8'), ('6230968', '8'), ('285671', '9'), ('285672', '9'), ('285673', '9'), ('285674', '9'), ('285679', '8'), ('285680', '8'), ('285681', '8'), ('285682', '8'), ('1202682', '8'), ('4803065', '8'), ('284512', '8'), ('284513', '8'), ('284514', '8'), ('2424221', '8'), ('284412', '9'), ('284413', '9'), ('284414', '9'), ('284415', '9'), ('284418', '9'), ('817829', '9'), ('8819671', '7'), ('1280064', '10'), ('7240460', '10'), ('10912901', '10'), ('586519', '9'), ('2315156', '9'), ('284878', '9'), ('3988787', '9'), ('2974741', '9'), ('7287573', '9'), ('11574871', '9'), ('287427', '7'), ('287428', '8'), ('287429', None), ('287430', '7'), ('287067', '8'), ('287068', '8'), ('285468', '10'), ('285469', '10'), ('285470', '10'), ('285471', '10'), ('10600260', '9'), ('14595588', '9'), ('285633', None), ('285634', None), ('285635', None), ('285636', None), ('285637', None), ('285638', None), ('285639', None), ('286178', '8'), ('286179', '8'), ('286180', '8'), ('286181', '8'), ('286182', '8'), ('286183', '8'), ('9449805', '8'), ('286465', '8'), ('285540', '9'), ('285541', '8'), ('285542', '8'), ('10222535', '8'), ('12683554', '9'), ('21258886', '9'), ('285908', None), ('285909', None), ('285910', None), ('285911', None), ('285912', None), ('285913', None), ('285914', None), ('285915', None), ('285916', None), ('285917', None), ('285918', None), ('285919', None), ('285920', None), ('285921', None), ('285922', None), ('285923', None), ('285924', None), ('285925', None), ('285926', '10'), ('288719', None), ('288720', None), ('288721', None)]
# print(len(SERIES_DATA))
# print(len(HREF_LIST))
#print(HEADERS)

#print(LIST)

#print(vlad_url)
#print(ilya_url)
