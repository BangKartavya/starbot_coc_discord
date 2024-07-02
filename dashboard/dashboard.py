from quart import Quart,redirect,url_for,render_template,request
from quart_discord import DiscordOAuth2Session,requires_authorization
import dotenv,os
from clash_of_clans_wrapper.player import Player
from clash_of_clans_wrapper.clan import Clan

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# discord_client_id = os.getenv("DISCORD_CLIENT_ID")
# discord_client_secret = os.getenv("DISCORD_CLIENT_SECRET")
# discord_redirect_uri = os.getenv("DISCORD_REDIRECT_URI")
# discord_bot_token = os.getenv("BOT_API_KEY")


app = Quart(__name__)
app.secret_key = b"abcd1234"
app.config["DISCORD_CLIENT_ID"] = 704389288955084841    
app.config["DISCORD_CLIENT_SECRET"] = "EHNs9kcU9cG4BP2OU7v3Pdi1bJt8QmWL"
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"                  
app.config["DISCORD_BOT_TOKEN"] = "NzA0Mzg5Mjg4OTU1MDg0ODQx.GdoY31.xz_7F9Chm124VQKHEF8f5zajzn5UHIwmJsfhMk"

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
    player = Player(player_tag)
    data = {
        "Player Name" : player.name,
        "Player Tag" : player.tag,
        "Player Town Hall Level" : player.townHallLevel,
        "Player Exp Level" : player.expLevel,
        "Player Trophies" : player.trophies,
        "Player Best Trophies" : player.bestTrophies,
        "Player War Stars" : player.warStars,
        "Player Attack Wins" : player.attackWins,
        "Player Defense Wins" : player.defenseWins,
        "Player Builder Hall Level" : player.builderHallLevel,
        "Player Best Builder Base Trophies" : player.bestBuilderBaseTrophies,
        "Player Role" : player.role,
        "Player War Preference" : player.warPreference,
        "Player Donations" : player.donations,
        "Player Clan Capital Contributions" : player.clanCapitalContributions
    }
    return await render_template('player_info/success.html',player_info = data)

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