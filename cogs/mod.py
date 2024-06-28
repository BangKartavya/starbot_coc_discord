from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client: commands.Bot = client

    
    @commands.command()
    @commands.is_owner()
    async def reload(self,ctx:commands.Context):
        exts = list(self.client.extensions.keys())
        for i in exts:
            self.client.reload_extension(i)
            await ctx.send(f"Reloaded Extension : {i}")
    @commands.command()
    @commands.is_owner()
    async def restart(self,ctx:commands.Context):
        await ctx.send("Restarting...")
        raise KeyboardInterrupt()



def setup(client:commands.Bot):
    client.add_cog(Moderation(client))