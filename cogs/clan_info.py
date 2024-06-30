import discord
from discord.ext import commands
from discord.ext.pages import Page,Paginator
from clash_of_clans_wrapper.clan import Clan
from clash_of_clans_wrapper.clan_war_log import WarLogList
from clash_of_clans_wrapper.capital_raid import CapitalRaidList
from clash_of_clans_wrapper.helper_error import AttackerNotFound

class ClanInfo(commands.Cog):
    def __init__(self,client):
        self.client: commands.Bot = client

    @commands.command(aliases = ['cinfo'],description = "Gets info about a clan with the clan tag")
    async def clan_info(self,ctx:commands.Context,clan_tag = '2G9LG9VCY'):
        if clan_tag[0] == '#':
            clan_tag = clan_tag[1:]
        clan = Clan(clan_tag)

        embed = discord.Embed(title=f'Info about {clan.name}',color= discord.Color.random())
        embed.add_field(name="Name",value=clan.name)
        embed.add_field(name="Type",value=clan.type)
        embed.add_field(name="description",value=clan.description)
        embed.add_field(name="Location",value=clan.location.name)
        embed.add_field(name="Is Family Friendly",value=clan.isFamilyFriendly)
        embed.add_field(name="Clan Level",value=clan.clanLevel)
        embed.add_field(name="Clan Points",value=clan.clanPoints)
        embed.add_field(name="clan Builder Base Points",value=clan.clanBuilderBasePoints)
        embed.add_field(name="Clan Capital Points",value=clan.clanCapitalPoints)
        embed.add_field(name="Clan Capital League",value=clan.capitalLeague.name)
        embed.add_field(name="Required Trophies",value=clan.requiredTrophies)
        embed.add_field(name="War Frequencies",value=clan.warFrequency)
        embed.add_field(name="War Win Streak",value=clan.warWinStreak)
        embed.add_field(name="war Wins",value=clan.warWins)
        embed.add_field(name="Is War Log Public?",value=clan.isWarLogPublic)
        embed.add_field(name="War League",value=clan.warLeague.name)
        embed.add_field(name="Members",value=clan.members)
        embed.add_field(name="Required Builder Base Trophies",value=clan.requiredBuilderBaseTrophies)
        embed.add_field(name="Required Town Hall",value=clan.requiredTownhallLevel)
        embed.add_field(name="Chat Language",value=clan.chatLanguage.name)

        await ctx.send(embed=embed)

    @commands.command(aliases = ['minfo'],description = "Get info about all the clan members with the clan tag")
    async def member_info(self,ctx:commands.Context,clan_tag = '2G9LG9VCY'):
        if clan_tag[0] == '#':
            clan_tag = clan_tag[1:]

        clan = Clan(clan_tag)
        my_pages = []
        for mem in clan.memberList:
            embed = discord.Embed(title="Members",color=discord.Color.random())
            embed.add_field(name = 'Tag',value=mem.tag)
            embed.add_field(name = 'Name',value=mem.name)
            embed.add_field(name = 'Clan Rank',value=mem.clanRank)
            embed.add_field(name = 'Role',value=mem.role)
            embed.add_field(name = 'Builder Base League',value=mem.builderBaseLeague.name)
            embed.add_field(name = 'Builder Base Trophies',value=mem.builderBaseTrophies)
            embed.add_field(name = 'Donations',value=mem.donations)
            embed.add_field(name = 'Donation Received',value=mem.donationsReceived)
            embed.add_field(name = 'EXP Level',value=mem.expLevel)
            embed.add_field(name = 'League',value=mem.league.name)
            embed.add_field(name = 'Name',value=",".join([f"{i.type} | {i.id}" for i in mem.playerHouse]))
            embed.add_field(name = 'Town Hall',value=mem.townHallLevel)
            embed.add_field(name = 'Previous Clan Rank',value=mem.previousClanRank)
            
            my_pages.append(Page(embeds=[embed]))
        paginator = Paginator(pages=my_pages)
        await paginator.send(ctx)

    @commands.command(alises = ['warlog'],description = "Get a clan's warlog with the tag and a limit of how many wars to show")
    async def clan_war_log(self,ctx:commands.Context,clan_tag = '2RCPQOLLQ',limit: int = 2):
        if clan_tag[0] == '#':
            clan_tag = clan_tag[1:]
        my_pages = []
        clan = WarLogList(clan_tag,limit)

        for war_log_item in clan.warLog:
            embed = discord.Embed(title="Warlog",color=discord.Color.random())
            embed.add_field(name='Result',value=war_log_item.result)
            embed.add_field(name='End Time',value=war_log_item.endTime)
            embed.add_field(name='Team Size',value=war_log_item.teamSize)
            embed.add_field(name='Attacks per Member',value=war_log_item.attacksPerMember,inline=False)
            embed.add_field(name='Clan Attacks',value=war_log_item.clan.attacks)
            embed.add_field(name='Clan Stars Earned',value=war_log_item.clan.stars)
            embed.add_field(name='Clan Destruction Percentage',value=war_log_item.clan.destructionPercentage)
            embed.add_field(name='Clan EXP Earned',value=war_log_item.clan.expEarned,inline=False)
            embed.add_field(name='Opponent Tag',value=war_log_item.opponent.tag)
            embed.add_field(name='Opponent Name',value=war_log_item.opponent.name)
            embed.add_field(name='Opponent Clan Level',value=war_log_item.opponent.clanLevel)
            embed.add_field(name='Opponent Stars Earned',value=war_log_item.opponent.stars)
            embed.add_field(name='Opponent Destruction Percentage',value=war_log_item.opponent.destructionPercentage)
            my_pages.append(Page(embeds=[embed]))
        
        paginator = Paginator(pages=my_pages)
        await paginator.send(ctx)

class ClanCapitalInfo(commands.Cog):
    def __init__(self,client):
        self.client: commands.Bot = client

    @commands.command(aliases = ['capinfo'],description = "Get the clan capital raid information of a clan")
    async def capital_info(self,ctx:commands.Context,clan_tag = '2G9LG9VCY',limit:int = 2):
        if clan_tag[0] == '#':
            clan_tag = clan_tag[1:]
        capital_raid_list = CapitalRaidList(clan_tag,limit)
        my_pages = []

        for i in capital_raid_list.capitalRaids:
            embed = discord.Embed(title="Capital Raid Info",color=discord.Color.random())    
            embed.add_field(name = "State",value = i.state,inline=False)
            embed.add_field(name = "Start Time",value = i.startTime)
            embed.add_field(name = "End Time",value = i.endTime)
            embed.add_field(name = "Capital Total Loot",value = i.capitalTotalLoot)
            embed.add_field(name = "Raids Completed",value = i.raidsCompleted)
            embed.add_field(name = "Total Attacks",value = i.totalAttacks)
            embed.add_field(name = "Enemy Districts Destroyed",value = i.enemyDistrictsDestroyed)
            embed.add_field(name = "Offensive Reward",value = i.offensiveReward)
            embed.add_field(name = "Defensive Reward",value = i.defensiveReward)
            my_pages.append(Page(embeds=[embed]))

        paginator = Paginator(pages=my_pages)
        await paginator.send(ctx)

    @commands.command(aliases = ['attlog'],description = "Get attack log of the raid weekend")
    async def attack_log(self,ctx:commands.Context,clan_tag = '2G9LG9VCY',limit:int = 2):
        if clan_tag[0] == '#':
            clan_tag = clan_tag[1:]
        capital_raid_list = CapitalRaidList(clan_tag,limit)
        my_pages = []

        for i in capital_raid_list.capitalRaids:
            for j in i.attackLog:
                embed = discord.Embed(title="Attack Logs",color = discord.Color.random())
                embed.add_field(name = 'Defender Tag', value = j.defender.tag)
                embed.add_field(name = 'Defender Name', value = j.defender.name)
                embed.add_field(name = 'Defender Level', value = j.defender.level)
                embed.add_field(name = 'Attack Count', value = j.attackCount)
                embed.add_field(name = 'District Count', value = j.districtCount)
                embed.add_field(name = 'District Destroyed', value = j.districtsDestroyed)
                my_pages.append(Page(embeds=[embed]))
        
        paginator = Paginator(pages=my_pages)

        await paginator.send(ctx)
    
    @commands.command(aliases = ['pattlog'],description = "Get player specific attack log in raid weekend") 
    async def player_attack_log(self,ctx:commands.Context,clan_tag = '2G9LG9VCY',player_tag = 'QU0LRPGP2',limit: int = 2):
        if clan_tag[0] == '#':
            clan_tag = clan_tag[1:]
        capital_raid_list = CapitalRaidList(clan_tag,limit)
        my_pages = []

        for capital_raid in capital_raid_list.capitalRaids:
            for attacks in capital_raid.attackLog:
                for district in attacks.districts:
                    for attack in district.attacks:
                        if attack.attacker.tag.split("#")[1] == player_tag:
                            embed = discord.Embed(title=f"Attack log of {attack.attacker.name}",color=discord.Color.random())
                            embed.add_field(name = 'District ID',value=district.id)
                            embed.add_field(name = 'District Name',value=district.name,inline=False)
                            embed.add_field(name = 'Attacker Tag',value=attack.attacker.tag)
                            embed.add_field(name = 'Attacker Name',value=attack.attacker.name)
                            embed.add_field(name = 'Attacker Destruction Percentage',value=attack.destructionPercent)
                            embed.add_field(name = 'Attacker Stars',value=attack.stars)
                            my_pages.append(Page(embeds=[embed]))
        
        if len(my_pages)==0:
            raise AttackerNotFound(message="Attacker Not Found")
        else:
            paginator = Paginator(pages=my_pages)
            await paginator.send(ctx)

    

def setup(client:commands.Bot):
    client.add_cog(ClanInfo(client))
    client.add_cog(ClanCapitalInfo(client))