from clash_of_clans_wrapper.player import Player
from clash_of_clans_wrapper.clan import Clan
from clash_of_clans_wrapper.capital_raid import CapitalRaidList
from clash_of_clans_wrapper.helper import Leagues,CapitalLeagues
from clash_of_clans_wrapper.clan_war_log import WarLogList
from datetime import datetime
import json

with open('./coc_api_wrapper_token_gen/key_created.json') as f:
    token = json.load(f)['key']['key']
    print(token)

clan = WarLogList()


capital_raid_list = CapitalRaidList('2G9LG9VCY')

# for i in capital_raid_list.objs:
#     print(i.attackLog)

# print("start time : ",datetime.fromisoformat('20240621T070000.000Z'))
# print("end time : ",datetime.fromisoformat('20240624T070000.000Z'))


# print(clan.tag)
# print(clan.name)
# print(clan.type)
# print(clan.description)

# print(clan.location)
# print(clan.location.id)
# print(clan.location.name)
# print(clan.location.isCountry)
# print(clan.location.countryCode)

# print(clan.isFamilyFriendly)
# print(clan.badgeUrl_small)
# print(clan.badgeUrl_large)
# print(clan.badgeUrl_medium)
# print(clan.clanLevel)
# print(clan.clanPoints)
# print(clan.clanBuilderBasePoints)
# print(clan.clanCapitalPoints)

# print(clan.capitalLeague)
# print(clan.capitalLeague.id)
# print(clan.capitalLeague.name)

# print(clan.requiredTrophies)
# print(clan.warFrequency)
# print(clan.warWinStreak)
# print(clan.isWarLogPublic)

# print(clan.warLeague)
# print(clan.warLeague.id)
# print(clan.warLeague.name)

# print(clan.members)

# print(clan.memberList)
# for i in clan.memberList:
#     print(i.tag)
#     print(i.name)
#     print(i.role)
#     print(i.townHallLevel)
#     print(i.expLevel)
#     print(i.league)
#     print(i.trophies)
#     print(i.builderBaseTrophies)
#     print(i.clanRank)
#     print(i.previousClanRank)
#     print(i.donations)
#     print(i.donationsReceived)
    
#     print(i.playerHouse)
#     if i.playerHouse:
#         for j in i.playerHouse:
#             print(j.type)
#             print(j.id)


#     print(i.builderBaseLeague)
#     print(i.builderBaseLeague.id)
#     print(i.builderBaseLeague.name)

# print(clan.labels)

# for i in clan.labels:
#     print(i.id)
#     print(i.name)
#     print(i.icon_small)
#     print(i.icon_medium)

# print(clan.requiredBuilderBaseTrophies)
# print(clan.requiredTownhallLevel)

# print(clan.clanCapital)
# print(clan.clanCapital.capitalHallLevel)

# print(clan.clanCapital.districts)

# for i in clan.clanCapital.districts:
#     print(i.id)
#     print(i.name)
#     print(i.districtHallLevel)

# print(clan.chatLanguage)
# print(clan.chatLanguage.id)
# print(clan.chatLanguage.name)
# print(clan.chatLanguage.languageCode)

league_list = CapitalLeagues(100)

for i in league_list.items:
    print(i.id)
    print(i.name)