import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

espn_home = "https://www.espn.com"
espn_base = "https://www.espn.com/college-football/team/schedule/_/id/84/season/"
seasonlist = [espn_base + str(n) for n in range(2003, 2020)]
pbpbase = "https://www.espn.com/college-football/playbyplay?gameId="
sched = requests.get(espn_base).text
soup = bs(sched, "html.parser")
season_games = soup.find_all("tbody", {"class": "Table__TBODY"})

masterlist = list()
for game in season_games:
    for g in game.find_all('a'):
        masterlist.append(g['href'])

opponentslist = list()
game_id_list = list()
for item in masterlist:
    if "gameId" in item:
        gameid = pbpbase + item.split("/gameId/")[1]
        if gameid not in game_id_list:
            game_id_list.append(gameid)
    elif "team/_/id" in item and espn_base + item not in opponentslist:
        opponentslist.append(espn_base + item)

