import discord
from discord.ext import commands
from clash_of_clans_wrapper.player import Player
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


def setup(client):
    client.add_cog(Player_Cmds(client))