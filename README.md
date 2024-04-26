# Парсер фильмов для проекта https://github.com/VDronovVladislav/best_movie
Парсер предназначен для сайта mustapp.com и парсит просмотренные пользователями фильмы,  после чего создает БД из фильмов, которые были просмотрены всеми участниками без исключения (т.е в итоговой БД не будет фильма, который не смотрел хотя бы один из участников, для которого проводился парсинг).
## Cтек:
BeautifulSoup, Selenium, SQLAlchemy.
## Инструкция по запуску:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VDronovVladislav/must_movie_parser
```
```
cd must_movie_parser
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```

  

* Если у вас Linux/macOS

  

```
source venv/bin/activate
```

  

* Если у вас windows

  

```
source venv/Scripts/activate
```

  

Установить зависимости из файла requirements.txt:

  

```
python3 -m pip install --upgrade pip
```

  

```
pip install -r requirements.txt
```

Запуск проекта - просто запуск файла must_selenium.py в IDE либо через терминал:

```
pyhton3 must_selenium.py
```

  ## Инструкция по работе с парсером:

В файле ```constants.py```  добавьте константы такого вида:
```
USERNAME_URL  =  '@username/watched'
username_url = urljoin(MAIN_URL, USERNAME_URL)
```
Также обязательно добавьте переменные с финальными url в список URL_LIST. Пример:
```
URL_LIST  = [username1_url, username1_url, username1_url]
```
Если вы хотите играть только по своим фильмам - просто добавьте в финальный ```URL_LIST``` только свой url.

В файле ```constants.py``` уже хранятся данные для примера. Это url со страницами просмотренных фильмов моих друзей и меня.

После того, как парсер отработает, будет создан файл базы данных ```db.sqlite3```.
Перенесите этот файл в папку ```/best_movie_app``` проекта best_movie и можно играть.