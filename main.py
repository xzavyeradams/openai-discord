# Xzavyer A. // xzavyer.dev
# https://github.com/xzavyeradams/openai-discord

import discord
import json
import sys
from discord.ext import commands

# attempts to load the config file
try:
    config = json.load(open("config.json", "r"))
except FileNotFoundError:
    input("Please run the setup first, refer to the github repo.")
    sys.exit(0)

# defines client
client = commands.Bot("a!", help_command=None)

@client.event
async def on_ready():
    print("Bot is online & logged in")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="xzavyer.dev/github"))
    # load cogs here

print("\n\ngithub.com/xzavyeradams/openai-discord")
client.run(config["token"])