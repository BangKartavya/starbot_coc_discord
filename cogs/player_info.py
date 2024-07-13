import discord
from discord.ext import commands
from clash_of_clans_wrapper.player import Player
from clash_of_clans_wrapper.rankings import PlayerRankingList
from clash_of_clans_wrapper.locations import Locations
from discord.ext.pages import Paginator,Page

class Player_Cmds(commands.Cog):
    def __init__(self,client):
        self.client: commands.Bot = client
    

    @commands.command(aliases = ['pinfo'],description = "Get information about a player using their tag")
    async def player_info(self,ctx:commands.Context,player_tag = 'QU0LRPGP2'):
        if player_tag[0] == "#":
            player_tag = player_tag[1:]
        player = Player(player_tag)
        embed = discord.Embed(title="Player Info",color=discord.Color.red())
        embed.add_field(name="**Name**", value=player.name)
        embed.add_field(name="**Town Hall**", value=player.townHallLevel)
        embed.add_field(name="**XP Level**", value=player.expLevel)
        embed.add_field(name="**Trophies**", value=player.trophies)
        embed.add_field(name="**Best Trophies**", value=player.bestTrophies)
        embed.add_field(name="**War Stars**", value=player.warStars)
        embed.add_field(name="**Attack Wins**", value=player.attackWins)
        embed.add_field(name="**Defense Wins**", value=player.defenseWins)
        embed.add_field(name="**Builder Hall Level**", value=player.builderHallLevel)
        embed.add_field(name="**Best Builder base trophies**", value=player.bestBuilderBaseTrophies)
        embed.add_field(name="**Role**", value=player.role)
        embed.add_field(name="**War Preference**", value=player.warPreference)
        embed.add_field(name="**Donations**", value=player.donations)
        embed.add_field(name="**Clan Capital Contributions**", value=player.clanCapitalContributions)
        # embed.add_field(name="**League**", value=player.league)
        embed.add_field(name="**Builder Base League**", value=player.builderBaseLeague.name)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['tr'],description = "Get info about player's troops")
    async def troops(self,ctx:commands.Context,player_tag = 'QU0LRPGP2'):
        my_pages = []
        if player_tag[0] == "#":
            player_tag = player_tag[1:]
        player = Player(player_tag)

        for i in player.troops:
            embed = discord.Embed(title=f"Info about {player.name}'s Troops - {i.name}",color = discord.Color.random())
            embed.add_field(name = "Name", value = i.name,inline=False)
            embed.add_field(name = "Current Level", value = i.level,inline=False)
            embed.add_field(name = "Max Level", value = i.maxLevel,inline=False)
            embed.add_field(name = "Village", value = i.village,inline=False)
            page = Page(embeds=[embed])
            my_pages.append(page)

        paginator = Paginator(pages=my_pages)
        await paginator.send(ctx)
    
    @commands.command(aliases = ['he'],description = "Get info about player's heros")
    async def heros(self,ctx:commands.Context,player_tag = 'QU0LRPGP2'):
        if player_tag[0] == "#":
            player_tag = player_tag[1:]

        player = Player(player_tag)
        my_pages = []

        for i in player.heros:
            embed = discord.Embed(title=f"Info about {player.name}'s Heros - {i.name}",color = discord.Color.random())
            embed.add_field(name = "Name", value = i.name,inline=False)
            embed.add_field(name = "Current Level", value = i.level,inline=False)
            embed.add_field(name = "Max Level", value = i.maxLevel,inline=False)
            embed.add_field(name = "Village", value = i.village,inline=False)
            embed.add_field(name = "Equipped Equipment", value = f"{i.equipment[0].name},{i.equipment[1].name}",inline=False)
            page = Page(embeds=[embed])
            my_pages.append(page)

        paginator = Paginator(pages=my_pages)
        await paginator.send(ctx)

    @commands.command(aliases = ['equ'],description = "Get info about player's hero equipments")
    async def equipment(self,ctx:commands.Context,player_tag = 'QU0LRPGP2'):
        if player_tag[0] == "#":
            player_tag = player_tag[1:]
        player = Player(player_tag)
        my_pages = []

        for i in player.heroEquipment:
            embed = discord.Embed(title=f"Info about {player.name}'s Hero Equipment - {i.name}",color = discord.Color.random())
            embed.add_field(name = "Name", value = i.name,inline=False)
            embed.add_field(name = "Current Level", value = i.level,inline=False)
            embed.add_field(name = "Max Level", value = i.maxLevel,inline=False)
            embed.add_field(name = "Village", value = i.village,inline=False)
            page = Page(embeds=[embed])
            my_pages.append(page)

        paginator = Paginator(pages=my_pages)
        await paginator.send(ctx)
    @commands.command(aliases = ['sp'],description = "Get info about player's spells")
    async def spells(self,ctx:commands.Context,player_tag = 'QU0LRPGP2'):
        if player_tag[0] == '#':
            player_tag = player_tag[1:]
        
        player = Player(player_tag)
        my_pages = []

        for i in player.spells:
            embed = discord.Embed(title=f"Info about {player.name}'s Spells - {i.name}",color=discord.Color.random())
            embed.add_field(name="Name",value=i.name,inline=False)
            embed.add_field(name="Level",value=i.level,inline=False)
            embed.add_field(name="Max Level",value=i.maxLevel,inline=False)
            embed.add_field(name="VIllage",value=i.village,inline=False)
            my_pages.append(Page(embeds=[embed]))
        
        paginator = Paginator(pages=my_pages)

        await paginator.send(ctx)

    @commands.command(aliases = ['toprank'],description = "Get info about the top ranking players in a location")
    async def top_ranking(self,ctx:commands.Context,locationId: int = 32000008,limit:int = 2):
        locations = Locations()
        location = None
        for i in locations.locations:
            if i.id == locationId:
                location = i
                break
        if not location:
            await ctx.reply("You provided a wrong location ID. Check the id and try again")
            return
        rank_list = PlayerRankingList(locationId,limit)
        my_pages = []
        for i in rank_list.rankingList:
            embed = discord.Embed(title = f"Ranking List for Location - {location.name}",color=discord.Color.random())
            embed.add_field(name = 'Tag',value = i.tag,inline=False)
            embed.add_field(name = 'Name',value = i.name,inline=False)
            embed.add_field(name = 'Exp Level',value = i.expLevel,inline=False)
            embed.add_field(name = 'Trophies',value = i.trophies,inline=False)
            embed.add_field(name = 'Attack Wins',value = i.attackWins,inline=False)
            embed.add_field(name = 'Defense Wins',value = i.defenseWins,inline=False)
            embed.add_field(name = 'Rank',value = i.rank,inline=False)
            embed.add_field(name = 'Previous Rank',value = i.previousRank,inline=False)
            embed.add_field(name = 'Clan Tag',value = i.clan.tag,inline=False)
            embed.add_field(name = 'Clan Name',value = i.clan.name,inline=False)
            embed.add_field(name = 'League ID',value = i.league.id,inline=False)
            embed.add_field(name = 'League Name',value = i.league.name,inline=False)
            my_pages.append(Page(embeds=[embed]))
        
        paginator = Paginator(pages=my_pages)
        await paginator.send(ctx)

def setup(client):
    client.add_cog(Player_Cmds(client))