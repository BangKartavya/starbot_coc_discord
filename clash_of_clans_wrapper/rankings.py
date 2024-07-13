import requests
import os
import dotenv
from clash_of_clans_wrapper.helper import PlayerRanking

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

token = os.getenv('COC_API_KEY')

# example location id -> 32000008

class PlayerRankingList:
    def __init__(self,locationId: int = 32000008,limit: int = 2):
        self.locationId = locationId
        self.limit = limit
        headers = {"Authorization" : f"Bearer {token} "}
        r = requests.get(url=f'https://api.clashofclans.com/v1/locations/{self.locationId}/rankings/players?limit={self.limit}',headers=headers)
        self.j = r.json()
        self.rankingList = [PlayerRanking(i) for i in self.j['items']]

