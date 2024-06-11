from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt
import pandas as pd
import requests

nba_teams = teams.get_teams()

i = 0
team = nba_teams[0]
while team:
    if i == 3:
        break
    else:
        print(nba_teams[i])
    i = i + 1

def convertDictionariesToTable(dict):
    keys = dict[0].keys()
    result = {}
    # Appends keys only
    for key in keys:
        result[key] = []

    # Appends values
    for info in dict:
        for key, value in info.items():
            result[key].append(value)
    return result

nba_teams_table = convertDictionariesToTable(nba_teams)
print(nba_teams)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

nba_teams_df = pd.DataFrame(nba_teams_table)
print(nba_teams_df.head(3))
print(nba_teams_df[nba_teams_df["nickname"] == "Warriors"])

id_warriors = nba_teams_df[["id"]].iloc[0, 0]
print(id_warriors) # Can use also nba_teams_df[["id"]].values[0][0]

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
# print(gamefinder.get_json()) # Returns history of games played by Warriors

games = gamefinder.get_data_frames()[0] # More readable compared to json type
print(games.head())

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")

file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
print(games.head(3))

games_home = games[games["MATCHUP"] == "GSW vs. TOR"]
print(games_home.head(3))
print(games_home["PLUS_MINUS"].mean())
print(games_home["PTS"].mean())

games_away = games[games["MATCHUP"] == "GSW @ TOR"]
print(games_away.head(3))
print(games_away["PLUS_MINUS"].mean())
print(games_away["PTS"].mean())

fig, ax = plt.subplots()

games_home.plot(x="GAME_DATE", y="PLUS_MINUS", ax=ax, rot=45)
games_away.plot(x="GAME_DATE", y="PLUS_MINUS", ax=ax, rot=45)
ax.legend(["home-court", "away-from-home"])
plt.title("Golden State Warriors vs Toronto Warriors Score")
plt.tight_layout()
plt.show() # It shows that the Warriors had played better when its their home-based

