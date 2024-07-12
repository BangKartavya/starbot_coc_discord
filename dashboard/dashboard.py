from quart import Quart,redirect,url_for,render_template,request
from quart_discord import DiscordOAuth2Session,requires_authorization
import dotenv,os
from clash_of_clans_wrapper.player import Player
from clash_of_clans_wrapper.clan import Clan

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

discord_client_id = os.getenv("DISCORD_CLIENT_ID")
discord_client_secret = os.getenv("DISCORD_CLIENT_SECRET")
discord_redirect_uri = os.getenv("DISCORD_REDIRECT_URI")
discord_bot_token = os.getenv("BOT_API_KEY")
app_secret_key = os.getenv("APP_SECRET_KEY")

app = Quart(__name__)
app.secret_key = app_secret_key.encode('utf-8')
app.config["DISCORD_CLIENT_ID"] = discord_client_id    
app.config["DISCORD_CLIENT_SECRET"] = discord_client_secret
app.config["DISCORD_REDIRECT_URI"] = discord_redirect_uri
app.config["DISCORD_BOT_TOKEN"] = discord_bot_token

discord = DiscordOAuth2Session(app)
 

@app.route("/")
async def index():
    return await render_template('index.html',authorized = await discord.authorized)

@app.route("/login/")
async def login():
    return await discord.create_session()

@app.route("/callback/")
async def callback():
    await discord.callback()
    return redirect(url_for(".me"))

@app.route("/player/")
async def player():
    return await render_template('player_info/player_info.html',authorized = await discord.authorized)

@app.route("/player/<string:player_tag>")
async def player_info(player_tag = 'QU0LRPGP2'):

    return await render_template('player_info/player.html')

@app.route('/player/<string:player_tag>/troops')
async def player_troop_info(player_tag = 'QU0LRPGP2'):
    player = Player(player_tag)

    troops = []

    for i in player.troops:
        troops.append({"name":i.name,"level":i.level,"maxLevel":i.maxLevel,"village":i.village})



    return await render_template('player_info/troops.html',troops = troops)

@app.route('/player/<string:player_tag>/spells')
async def player_spell_info(player_tag = 'QU0LRPGP2'):
    player = Player(player_tag)

    spells = []

    for i in player.spells:
        spells.append({"name":i.name,"level":i.level,"maxLevel":i.maxLevel,"village":i.village})



    return await render_template('player_info/spells.html',spells = spells)


@app.route('/player/<string:player_tag>/achievements')
async def player_achievement_info(player_tag = 'QU0LRPGP2'):
    player = Player(player_tag)

    achievements = []

    for i in player.achievements:

        data = {
            "name":i.name,
            "info":i.info,
            "completionInfo":i.completionInfo,
            "stars":i.stars,
            "target":i.target,
            "value":i.value,
            "village":i.village
        }

        achievements.append(data)



    return await render_template('player_info/achievements.html',achievements = achievements)

@app.route('/clan/')
async def clan():
    return await render_template('clan_info/clan_info.html',authorized = await discord.authorized)

@app.route("/clan/<string:clan_tag>")
async def clan_info(clan_tag = '2G9LG9VCY'):
    clan = Clan(clan_tag)
    data = {
        "Clan Name" : clan.name,
        "Clan Type" : clan.type,
        "Clan Description" : clan.description,
        "Clan Is Family Friendly?" : clan.isFamilyFriendly,
        "Clan Clan Level" : clan.clanLevel,
        "Clan Clan Points" : clan.clanPoints,
        "Clan Clan Builder Base Points" : clan.clanBuilderBasePoints,
        "Clan Clan Capital Points" : clan.clanCapitalPoints,
        "Clan Required Trophies" : clan.requiredTrophies,
        "Clan War Frequency" : clan.warFrequency,
        "Clan War Win Streak" : clan.warWinStreak,
        "Clan War Wins" : clan.warWins,
        "Clan Is War Log Public?" : clan.isWarLogPublic,
        "Clan Members" : clan.members,
        "Clan Required Builder Base Trophies" : clan.requiredBuilderBaseTrophies,
        "Clan Required Town Hall Level" : clan.requiredTownhallLevel

    }
    return await render_template('clan_info/success.html',clan_info = data)

@app.route("/logout/")
async def logout():
    discord.revoke()
    return redirect(url_for(".index"))

@app.route("/me/")
@requires_authorization
async def me():
    user = await discord.fetch_user()
    return await render_template('dashboard.html',authorized = await discord.authorized)

if __name__ == "__main__":
    app.run(debug=True)