import discord
import os
from discord.activity import Game
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

# deafult prefix
client = commands.Bot(command_prefix='rr!')

# cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# login-event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f'on {len(client.guilds)} server | rr!help'))
    print("Logging in as {0.user}".format(client))


client.run(os.getenv('token'))
