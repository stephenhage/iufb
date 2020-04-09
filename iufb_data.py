import requests
from bs4 import BeautifulSoup as bs

espn_home = "https://www.espn.com"
espn_base = "https://www.espn.com/college-football/team/schedule/_/id/84/season/2019"

sched = requests.get(espn_base).text


soup = bs(sched, "html.parser")

with open("iusched.html", "w") as file:
    file.write(sched)

opponentslist = list()
gameslist = list()

# Get the schedule
season_games = soup.find_all("tbody", {"class": "Table__TBODY"})

# Record the opponent
def get_opponents(gameslist):
    for game in gameslist:
        for a in game.find_all("td"):
            outlink = a.find_all("a", {"class": "AnchorLink"})
            opponentslist.append(a.find('a', {"class": "AnchorLink"})['href'])
            for link in outlink:
                if "/team/" in link['href']:
                    opponentslist.append(espn_home + link['href'])
get_opponents(season_games)
print(opponentslist)