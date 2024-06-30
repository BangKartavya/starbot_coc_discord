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
    
    async def send_command_help(self, command:commands.Command):
        embed = discord.Embed(title = f"Information about command - {command.qualified_name}",color=discord.Color.random())

        if command.help:
            embed.description = command.help
        else:
            embed.description = command.description
        
        embed.add_field(name = 'Command Enabled',value=command.enabled)

        if alias := command.aliases:
            embed.add_field(name='Aliases',value=", ".join(alias),inline=False)

        embed.add_field(name = 'Arguments ',value=command.signature,inline=False)

        embed.add_field(name = 'Usage',value=f".{command.qualified_name}{'|' if alias else ''}{'|'.join(alias) if alias else ''} {command.signature}")

        await self.get_destination().send(embed=embed)