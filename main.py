import discord
from discord.ext import commands
import dotenv
import os
from cogs.help import MyHelp
from dynamic_token_gen.main import *

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv()

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

token = os.getenv('BOT_API_KEY')

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix='.',intents=intents)

client.load_extension('cogs.player_info')
client.load_extension('cogs.listeners')
client.load_extension('cogs.mod')
client.load_extension('cogs.clan_info')
client.load_extension('cogs.misc')

client.help_command = MyHelp()

if __name__ == "__main__":
    client.run(token)