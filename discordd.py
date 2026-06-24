import discord
from discord import app_commands
import random
TOKEN ="your_discord_token_here"
GUILD_ID="server guild id"
intents=discord.Intents.default()
intents.message_content=True
intents.members=True
bot = discord.Client(intents=intents)
tree=app_commands.CommandTree(bot)
@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Bot is online : {bot.user}")
def get_team_size(mode):
    number = int(mode.split("v")[0])
    return number * 2

def check_players(players, mode):
    return get_team_size(mode) == len(players)

def make_teams(players):
    random.shuffle(players)
    half = len(players) // 2
    return players[:half], players[half:]
current_game = None
players = []  
@tree.command(name="start",description="start a mini game",guild=discord.Object(id=GUILD_ID))
@app_commands.choices(mode=[
    app_commands.Choice(name="1v1",value="1v1"),
    app_commands.Choice(name="2v2",value="2v2"),
    app_commands.Choice(name="3v3",value="3v3"),
    app_commands.Choice(name="4v4",value="4v4"),
    app_commands.Choice(name="5v5",value="5v5"),
])
async def start(interaction: discord.Interaction , mode: app_commands.Choice[str]):
    global current_game , players
    current_game=mode.value
    players=[]
    size = get_team_size(current_game)
    await interaction.response.send_message(f"@everyone  \uFFFD {current_game} game started! Need {size} players. Type /join to enter!")
@tree.command(name="join" ,description="join the current game ",guild=discord.Object(id=GUILD_ID))
async def join(interaction :discord.Interaction):
    global players , current_game
    if current_game is None :
         await interaction.response.send_message("No game running! Admin must type /start first.")
         return
    username = interaction.user.mention
    if username in players:
        await interaction.response.send_message(f"{username} you already joined!")
        return
    players.append(username)
    if check_players(players, current_game):
        team1, team2 = make_teams(players.copy())
        team1_str = " ".join(team1)
        team2_str = " ".join(team2)
        await interaction.response.send_message(f"\uFFFD Teams ready!\n**Team 1:** {team1_str}\n**Team 2:** {team2_str}")
        current_game = None
        players = []
    else:
        size = get_team_size(current_game)
        await interaction.response.send_message(f"{username} joined! {len(players)}/{size} players ready.")
bot.run(TOKEN)
