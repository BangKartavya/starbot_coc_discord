from discord.ext import commands
import discord,dotenv,os
from dynamic_token_gen.main import get_keys,login,load,logout
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

    @commands.command()
    @commands.is_owner()
    async def keys(self,ctx:commands.Context):
        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)
        email = os.getenv('email')
        password = os.getenv('password')
        
        log = login(email,password)
        keys = get_keys(log)
        
        karnav = await self.client.fetch_user(ctx.message.author.id)
        
        for i in keys.json()['keys']:
            await karnav.send(f"Key - {i['key']}")
        
        logout(log)

def setup(client:commands.Bot):
    client.add_cog(Moderation(client))