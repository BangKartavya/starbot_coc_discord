import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client = client
    

    @commands.command()
    async def ping(self,ctx:commands.Context):
        await ctx.reply(f"{round(self.client.latency*1000)}ms")

    

def setup(client:commands.Bot):
    client.add_cog(Misc(client))