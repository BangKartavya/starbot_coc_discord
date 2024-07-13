import discord
from discord.ext import commands
from clash_of_clans_wrapper.locations import Locations
class Misc(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client = client
    

    @commands.command(description = "Get the latency of the bot")
    async def ping(self,ctx:commands.Context):
        await ctx.reply(f"{round(self.client.latency*1000)}ms")

    @commands.command(aliases = ['loc'],description = "Get location info from name")
    async def location(self,ctx:commands.Context,*,location_name:str):
        locations = Locations()

        for i in locations.locations:
            if i.name.lower() == location_name.lower():
                embed = discord.Embed(title = f"Info About {i.name}",color=discord.Color.random())
                embed.add_field(name = 'Name',value=i.name,inline=False)
                embed.add_field(name = 'ID',value=i.id,inline=False)
                embed.add_field(name = 'Is Country?',value=i.isCountry,inline=False)
                embed.add_field(name = 'Country Code',value=i.countryCode,inline=False)
                await ctx.send(embed=embed)
                return
        
        await ctx.reply("The country name provided is not correct.")



def setup(client:commands.Bot):
    client.add_cog(Misc(client))