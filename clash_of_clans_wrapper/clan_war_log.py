import requests
from dotenv import load_dotenv
import os
from datetime import datetime
from clash_of_clans_wrapper.helper_error import *
from clash_of_clans_wrapper.helper import WarLogItem
load_dotenv()

token = os.getenv("COC_API_KEY")

# Clan Tag -> #2RCPQOLLQ

class WarLogList:
    def __init__(self,tag = '2RCPQOLLQ',limit: int = 2):
        self.tag = tag
        headers = {'Authorization': f"Bearer {token}"}
        r = requests.get(url = f'https://api.clashofclans.com/v1/clans/%23{self.tag}/warlog?limit={limit}',headers=headers)
        self.j = r.json()
        if r.status_code == 403:
            raise InvalidAuth(self.j['reason'],self.j['message'])
        elif r.status_code == 404:
            raise NotFound(self.j['reason'])
        elif r.status_code == 503:
            raise UnderMaintainance(self.j['reason'])
        else:
            self.warLog = [WarLogItem(i) for i in self.j['items']] 






