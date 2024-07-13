import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("COC_API_KEY_2")


class ClanName:
    def __init__(self,j):
        self.tag = j['tag']
        self.name = j['name']
        self.clanLevel = j['clanLevel']
        self.badgeUrl_small = j['badgeUrls']['small']
        self.badgeUrl_large = j['badgeUrls']['large']
        self.badgeUrl_medium = j['badgeUrls']['medium']

class Spell:
    def __init__(self,j):
        self.name = j['name']
        self.level = j['level']
        self.maxLevel = j['maxLevel']
        self.village = j['village']

class PlayerHouseElement:
    def __init__(self,j=None):
        if not j:
            self.type = ""
            self.id = 0
        else:
            self.type = j['type']
            self.id = j['id']

class Label:
    def __init__(self,j):
        self.id = j['id']
        self.name = j['name']
        self.icon_small = j['iconUrls']['small']
        self.icon_medium = j['iconUrls']['medium']

class League:
    def __init__(self,j):
        self.id = j['id']
        self.name = j['name']
        try:
            self.icon_small = j['iconUrls']['small']
        except KeyError:
            self.icon_small = None
        try:
            self.icon_tiny = j['iconUrls']['tiny']
        except KeyError:
            self.icon_tiny = None
        try:
            self.icon_medium = j['iconUrls']['medium']
        except KeyError:
            self.icon_medium = None

class BuilderBaseLeague:
    def __init__(self,j):
        self.id = j['id']
        self.name = j['name']

class Achievement:
    def __init__(self,j):
        self.name = j['name']
        self.stars = j['stars']
        self.value = j['value']
        self.target = j['target']
        self.info = j['info']
        self.completionInfo = j['completionInfo']
        self.village = j['village']

class Troop:
    def __init__(self,j):
        self.name = j['name']
        self.level = j['level']
        self.maxLevel = j['maxLevel']
        self.village = j['village']

class Equipment:
    def __init__(self,j= None):

        if not j:
            self.name = None
            self.level = None
            self.maxLevel = None
            self.village = None
        else:
            self.name = j['name']
            self.level = j['level']
            self.maxLevel = j['maxLevel']
            self.village = j['village']

class Heros:
    def __init__(self,j):
        self.name = j['name']
        self.level = j['level']
        self.maxLevel = j['maxLevel']
        try:
            self.equipment = [Equipment(j['equipment'][0]),Equipment(j['equipment'][1])]
        except KeyError:
            self.equipment = [Equipment(),Equipment()]
        self.village = j['village']

class Language:
    def __init__(self,j):
        self.id = j['id']
        self.name = j['name']
        self.languageCode = j['languageCode']

class ClanInfoDistrict:
    def __init__(self,j):
        self.id = j['id']
        self.name = j['name']
        self.districtHallLevel = j['districtHallLevel']

class ClanCapital:
    def __init__(self,j):
        self.capitalHallLevel = j['capitalHallLevel']
        self.districts = [ClanInfoDistrict(i) for i in j['districts']]

class ClanMember:
    def __init__(self,j):
        self.tag = j['tag']
        self.name = j['name']
        self.role = j['role']
        self.townHallLevel = j['townHallLevel']
        self.expLevel = j['expLevel']
        self.league = League(j['league'])
        self.trophies = j['trophies']
        self.builderBaseTrophies = j['builderBaseTrophies']
        self.clanRank = j['clanRank']
        self.previousClanRank = j['previousClanRank']
        self.donations = j['donations']
        self.donationsReceived = j['donationsReceived']
        try:
            self.playerHouse = [PlayerHouseElement(i) for i in j['playerHouse']['elements']]
        except KeyError:
            self.playerHouse = [PlayerHouseElement()]
        self.builderBaseLeague = BuilderBaseLeague(j['builderBaseLeague'])
    
class WarLeague:
    def __init__(self,j):
        self.id = j['id']
        self.name = j['name']

class CapitalLeague:
    def __init__(self,j):
        self.id = j['id']
        self.name = j['name']

class Location:
    def __init__(self,j):
        self.id: int = j['id']
        self.name: str = j['name']
        self.isCountry: bool = j['isCountry']
        if self.isCountry:
            self.countryCode: str = j['countryCode']
        else:
            self.countryCode = None

class Leagues:
    def __init__(self,limit):
        self.limit = limit
        headers = {"Authorization" : f"Bearer {token} "}
        r = requests.get(url=f'https://api.clashofclans.com/v1/leagues?limit={self.limit}',headers=headers)
        self.j = r.json()   
        self.items = [League(i) for i in self.j['items']]

class CapitalLeagues:
    def __init__(self,limit):
        self.limit = limit
        headers = {"Authorization" : f"Bearer {token} "}
        r = requests.get(url=f'https://api.clashofclans.com/v1/capitalleagues?limit={self.limit}',headers=headers)
        self.j = r.json()
        self.items = [CapitalLeague(i) for i in self.j['items']]

class CapitalRaidMember:
    def __init__(self,j):
        self.tag: str = j['tag']
        self.name: str = j['name']
        self.attacks = j['attacks']
        self.bonusAttackLimit = j['bonusAttackLimit']
        self.capitalResourcesLooted = j['capitalResourcesLooted']

class Defender:
    def __init__(self,j):
        self.tag: str = j['tag']
        self.name: str = j['name']
        self.level: int  = j['level']
        self.badgeUrl_small: str = j['badgeUrls']['small']
        self.badgeUrl_large: str = j['badgeUrls']['large']
        self.badgeUrl_medium: str = j['badgeUrls']['medium']

class Attacker:
    def __init__(self,j):
        self.tag: str = j['tag']
        self.name: str = j['name']

class Attack:
    def __init__(self,j):
        self.attacker = Attacker(j['attacker'])
        self.destructionPercent: int = j['destructionPercent']
        self.stars: int = j['stars']

class District:
    def __init__(self,j):
        self.id:int = j['id']
        self.name: str = j['name']
        self.districtHallLevel: int = j['districtHallLevel']
        self.destructionPercent: int = j['destructionPercent']
        self.stars: int = j['stars']
        self.attackCount:int = j['attackCount']
        self.totalLooted: int = j['totalLooted']
        try:
            self.attacks = [Attack(i) for i in j['attacks']]
        except KeyError:
            self.attacks = []

class AttackLogElement:
    def __init__(self,j):
        self.defender = Defender(j['defender'])
        self.attackCount: int = j['attackCount']
        self.districtCount: int = j['districtCount']
        self.districtsDestroyed: int = j['districtsDestroyed']
        self.districts = [District(i) for i in j['districts']]



class DefenseLogElement:
    def __init__(self,j):
        self.attacker = Defender(j['attacker'])
        self.attackCount: int = j['attackCount']
        self.districtCount: int = j['districtCount']
        self.districtsDestroyed: int = j['districtsDestroyed']
        self.districts = [District(i) for i in j['districts']]


class CapitalRaid:
    def __init__(self,j):
        self.state: str = j['state']
        self.startTime: str = datetime.fromisoformat(j['startTime'])
        self.endTime: str = datetime.fromisoformat(j['endTime'])
        self.capitalTotalLoot: int = j['capitalTotalLoot']
        self.raidsCompleted: int = j['raidsCompleted']
        self.totalAttacks: int = j['totalAttacks']
        self.enemyDistrictsDestroyed: int = j['enemyDistrictsDestroyed']
        self.offensiveReward:int = j['offensiveReward']
        self.defensiveReward: int = j['defensiveReward']
        try:
            self.members = [CapitalRaidMember(i) for i in j['members']]
        except KeyError:
            self.members = []
        self.attackLog = [AttackLogElement(i) for i in j['attackLog']]
        self.defenseLog = [DefenseLogElement(i) for i in j['defenseLog']]

class WarClan(ClanName):
    def __init__(self, j):
        super().__init__(j)
        self.clanLevel: int = j['clanLevel']
        try:
            self.attacks: int = j['attacks']
        except:
            pass
        self.stars: int = j['stars']
        self.destructionPercentage = j['destructionPercentage']
        try:
            self.expEarned = j['expEarned']
        except KeyError:
            pass

class WarLogItem:
    def __init__(self,j):
        self.result:str = j['result']
        self.endTime = datetime.fromisoformat(j['endTime'])
        self.teamSize: int = j['teamSize']
        self.attacksPerMember: int = j['attacksPerMember']
        self.battleModifier: str = j['battleModifier']
        self.clan = WarClan(j['clan'])
        self.opponent = WarClan(j['opponent'])

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



