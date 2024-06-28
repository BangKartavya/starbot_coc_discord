import requests
import os
from clash_of_clans_wrapper.helper import *
from clash_of_clans_wrapper.helper_error import *
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("COC_API_KEY")


class Player:
    def __init__(self,tag = 'QU0LRPGP2'):
        self.tag = tag
        headers = {"Authorization" : f"Bearer {token} "}
        r = requests.get(f'https://api.clashofclans.com/v1/players/%23{self.tag}',headers=headers)
        self.j = r.json()
        
        if r.status_code == 403:
            raise InvalidAuth(self.j['reason'],self.j['message'])
        elif r.status_code == 404:
            raise NotFound(self.j['reason'])
        elif r.status_code == 503:
            raise UnderMaintainance(self.j['reason'])
        else:
            self.name = self.j['name']
            self.tag = self.j['tag']
            self.townHallLevel = self.j['townHallLevel']
            self.expLevel = self.j['expLevel']
            self.trophies = self.j['trophies']
            self.bestTrophies = self.j['bestTrophies']
            self.warStars = self.j['warStars']
            self.attackWins = self.j['attackWins']
            self.defenseWins = self.j['defenseWins']
            self.builderHallLevel = self.j['builderHallLevel']
            self.bestBuilderBaseTrophies = self.j['bestBuilderBaseTrophies']
            self.role = self.j['role']
            self.warPreference = self.j['warPreference']
            self.donations = self.j['donations']
            self.clanCapitalContributions = self.j['clanCapitalContributions']
            self.clan = ClanName(self.j['clan'])
            # self.league = League(self.j['league'])
            self.builderBaseLeague = BuilderBaseLeague(self.j['builderBaseLeague'])
            self.achievements = self.get_achievements()
            self.playerHouse = self.get_player_house()
            self.labels = self.get_labels()
            self.troops = self.get_troops()
            self.heros = self.get_heros()
            self.heroEquipment = self.get_hero_equipment()
            self.spells = self.get_spells()


    def get_achievements(self) -> list[Achievement]:
        return [Achievement(i) for i in self.j['achievements']]
    
    def get_troops(self) -> list[Troop]:
        return [Troop(i) for i in self.j['troops']]
    
    def get_heros(self) -> list[Heros]:
        return [Heros(i) for i in self.j['heroes']]
    
    def get_hero_equipment(self) -> list[Equipment]:
        return [Equipment(i) for i in self.j["heroEquipment"]]

    def get_labels(self) -> list[Label]:
        return [Label(i) for i in self.j['labels']]

    def get_player_house(self) -> list[PlayerHouseElement]:
        return [PlayerHouseElement(i) for i in self.j['playerHouse']['elements']]

    def get_spells(self) -> list[Spell]:
        return [Spell(i) for i in self.j['spells']]
