import requests
import os
import dotenv
from clash_of_clans_wrapper.helper import League

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

token = os.getenv('COC_API_KEY')

# example location id -> 32000008

class PlayerRankingClan:
    def __init__(self,j):
        self.tag = j['tag']
        self.name = j['name']
        try:
            self.badge_url_small = j['badgeUrl']['small']
        except KeyError:
            self.badge_url_small = None
        try:
            self.badge_url_large = j['badgeUrl']['large']
        except KeyError:
            self.badge_url_large = None
        try:

            self.badge_url_medium = j['badgeUrl']['medium']
        except KeyError:
            self.badge_url_medium = None

class PlayerRanking:
    def __init__(self,j):
        self.league = League(j['league'])
        self.clan = PlayerRankingClan(j['clan'])
        self.attackWins = j['attackWins']
        self.defenseWins = j['defenseWins']
        self.tag = j['tag']
        self.name = j['name']
        self.expLevel = j['expLevel']
        self.rank = j['rank']
        self.previousRank = j['previousRank']
        self.trophies = j['trophies']

class PlayerRankingList:
    def __init__(self,locationId: int = 32000008,limit: int = 2):
        self.locationId = locationId
        self.limit = limit
        headers = {"Authorization" : f"Bearer {token} "}
        r = requests.get(url=f'https://api.clashofclans.com/v1/locations/{self.locationId}/rankings/players?limit={self.limit}',headers=headers)
        self.j = r.json()
        self.rankingList = [PlayerRanking(i) for i in self.j['items']]

