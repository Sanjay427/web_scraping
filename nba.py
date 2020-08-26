# !usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs
from user_database import Database


def get_player_info():
    base_url = 'https://www.nba.com'
    url = 'https://www.nba.com/players'
    response = requests.get(url)
    if response.status_code == 200:
        print('connection successful')
    page_source = bs(response.content, 'lxml')
    user_name_info = page_source.select('section.nba-player-index__trending-item')
    player_info = {}
    for info in user_name_info:
        player_rank = int(info.next.text)
        player_info_link = base_url + info.a['href']
        player_name = info.find('p', class_='nba-player-index__name').text
        image_div = info.find('div', class_='nba-player-index__headshot_wrapper')
        image_url = 'https:' + image_div.img.get('data-src')
        position_div = info.find("div", class_='nba-player-index__details')
        player_position = position_div.find_next().text
        height_span = position_div.find_next().find_next().text
        player_height = height_span[:height_span.index('|')]
        player_info[player_name] = [player_rank,
                                    player_position,
                                    image_url,
                                    player_height,
                                    player_info_link]

    return player_info


def insert_player_info(player_info):
    database = Database()
    database.create_table()
    id = 1
    for key, value in player_info.items():
        values = (id, key, *value)
        database.insert_into_table(values)
        id += 1
