from discord.ext import commands
import discord,dotenv,os
from dynamic_token_gen.main import *

class Moderation(commands.Cog):
    def __init__(self,client:commands.Bot):
        self.client: commands.Bot = client

    
    @commands.command(aliases = ["re"],description = "ONLY FOR OWNER... reloads the cogs")
    @commands.is_owner()
    async def reload(self,ctx:commands.Context):
        exts = list(self.client.extensions.keys())
        for i in exts:
            self.client.reload_extension(i)
            await ctx.send(f"Reloaded Extension : {i}")

    @commands.command(aliases = ["res"],description = "ONLY FOR OWNER... Restarts the bot")
    @commands.is_owner()
    async def restart(self,ctx:commands.Context):
        await ctx.send("Restarting...")
        raise KeyboardInterrupt()

    @commands.command(aliases = ["key"],description = "ONLY FOR OWNER... get the api keys for a session")
    @commands.is_owner()
    async def keys(self,ctx:commands.Context):
        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)
        email = os.getenv('email')
        password = os.getenv('password')
        
        log = login(email,password)
        load(log)
        keys = get_keys(log)
        
        karnav = await self.client.fetch_user(ctx.message.author.id)
        
        for i in keys.json()['keys']:
            await karnav.send(f"Key - {i['key']}")
        
        logout(log)
    @commands.command(aliases = ["gk"],description = "ONLY FOW OWNER... generate api_key")
    @commands.is_owner()
    async def generate_key(self,ctx:commands.Context):
        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)
        email = os.getenv('email')
        password = os.getenv('password')

        log = login(email,password)
        ip = load(log).json()['developer']['prevLoginIp']

        token = get_key_with_ip(log,ip)

        if not token:
            remove_keys(log)
            token = create_key(log,'key','key',ip)

        logout(log)


        os.environ['COC_API_KEY'] = token

        dotenv.set_key(dotenv_file,'COC_API_KEY',os.environ['COC_API_KEY'])

def setup(client:commands.Bot):
    client.add_cog(Moderation(client))