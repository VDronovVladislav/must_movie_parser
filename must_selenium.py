import time

from selenium import webdriver
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from constants import URL_LIST
from models import Base, Movie


if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)
    overlap = set()

    for url in URL_LIST:
        movies_lst = []
        driver = webdriver.Chrome()
        driver.get(url)
        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(2)
            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )
            if new_height == last_height:
                break
            last_height = new_height
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, 'html.parser')
        content_div = soup.find('div', class_='profile__list_content js_items')
        poster_titles = content_div.find_all('div', class_='poster__title')
        poster_arts = content_div.find_all('div', class_='poster__art')

        for poster_title, poster_art in zip(poster_titles, poster_arts):
            title = poster_title.text
            href = poster_art['style'].split('"')[1]
            movies_lst.append((title, href))

        movies_set = set(movies_lst)

        if overlap:
            overlap = overlap & movies_set
        else:
            overlap = movies_set

    for movie in overlap:
        db_session = Session(engine)
        db_session.execute(
            insert(Movie).values(
                name=movie[0],
                image=movie[1]
            )
        )
        db_session.commit()
