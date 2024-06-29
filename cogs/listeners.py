import discord
from discord.ext import commands
from clash_of_clans_wrapper import helper_error

class Listeners(commands.Cog):
    def __init__(self,client):
        self.client: commands.Bot = client
    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user.name} is ready")
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx:commands.Context,error):
        if isinstance(error,helper_error.InvalidAuth):
            await ctx.reply(f"Command failed\nReason : {error.reason}\nMessage : {error.msg}")
        elif isinstance(error,commands.NotOwner):
            await ctx.reply("Only the owner can use this command")
        elif isinstance(error,helper_error.NotFound):
            await ctx.reply("Player/Clan with that ID was not found")
        elif isinstance(error,commands.CommandNotFound):
            await ctx.reply(error.args[0])
        elif isinstance(error,helper_error.AttackerNotFound):
            await ctx.reply(error.args[0])
        else:
            await ctx.reply(error.args[0])


def setup(client):
    client.add_cog(Listeners(client))