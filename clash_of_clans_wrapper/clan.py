import requests
import os
from clash_of_clans_wrapper.helper import Label,Location,CapitalLeague,WarLeague,ClanCapital,ClanMember,Language
from clash_of_clans_wrapper.helper_error import *
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("COC_API_KEY")

# CLAN TAG -> #2G9LG9VCY

class Clan:
    def __init__(self,tag = '2G9LG9VCY'):
        self.tag = tag
        headers = {"Authorization" : f"Bearer {token} "}
        r = requests.get(url = f'https://api.clashofclans.com/v1/clans/%23{self.tag}',headers=headers)
        self.j = r.json()
        if r.status_code == 403:
            raise InvalidAuth(self.j['reason'],self.j['message'])
        elif r.status_code == 404:
            raise NotFound(self.j['reason'])
        elif r.status_code == 503:
            raise UnderMaintainance(self.j['reason'])
        else:
            self.name = self.j['name']
            self.type = self.j['type']
            self.description = self.j['description']
            self.location = Location(self.j['location'])
            self.isFamilyFriendly = self.j['isFamilyFriendly']
            self.badgeUrl_small = self.j['badgeUrls']['small']
            self.badgeUrl_large = self.j['badgeUrls']['large']
            self.badgeUrl_medium = self.j['badgeUrls']['medium']
            self.clanLevel = self.j['clanLevel']
            self.clanPoints = self.j['clanPoints']
            self.clanBuilderBasePoints = self.j['clanBuilderBasePoints']
            self.clanCapitalPoints = self.j['clanCapitalPoints']
            self.capitalLeague = CapitalLeague(self.j['capitalLeague'])
            self.requiredTrophies = self.j['requiredTrophies']
            self.warFrequency = self.j['warFrequency']
            self.warWinStreak = self.j['warWinStreak']
            self.warWins = self.j['warWins']
            self.isWarLogPublic = self.j['isWarLogPublic']
            self.warLeague = WarLeague(self.j['warLeague'])
            self.members = self.j['members']
            self.memberList = [ClanMember(i) for i in self.j['memberList']]
            self.labels = [Label(i) for i in self.j['labels']]
            self.requiredBuilderBaseTrophies = self.j['requiredBuilderBaseTrophies']
            self.requiredTownhallLevel = self.j['requiredTownhallLevel']
            self.clanCapital = ClanCapital(self.j['clanCapital'])
            self.chatLanguage = Language(self.j['chatLanguage'])