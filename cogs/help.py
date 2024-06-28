from discord.ext import commands
import discord
from discord.ext.pages import Page,Paginator

class MyHelp(commands.HelpCommand):
    
    async def send_bot_help(self, mapping):
        my_pages = []
        for cog,commands in mapping.items():
            command_signatures = [self.get_command_signature(c) for c in commands]
            if command_signatures:
                embed = discord.Embed(title="Help",color=discord.Color.random())
                cog_name = getattr(cog,"qualified_name","No Category")
                embed.add_field(name = cog_name,value='\n'.join(command_signatures))
                my_pages.append(Page(embeds = [embed]))
        channel:discord.TextChannel = self.get_destination()
        paginator = Paginator(pages=my_pages)
        await paginator.send(self.context,target=channel)