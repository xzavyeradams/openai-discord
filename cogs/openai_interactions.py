# xzavyer.dev
import discord
import aiohttp
from discord import app_commands
from discord.ext import commands

# I apologize if any of this is incorrect, I'm on a chromebook at the time of this commit
# and don't have easy access to documentation or testing.

class GPT3(commands.GroupCog, name="gpt3", group_description="Generates text based content based on a prompt using AI."):
    def __init__(self, bot: commands.Bot, auth: str, tkn: int, org: str):
        self.bot = bot
        self.client = aiohttp.ClientSession()
        self.headers = {"Authorization": "Bearer " + auth}
        self.max = tkn
        self.org = org
        
        super().__init__()

    @app_commands.command(name="davinci", description="GPT-3 text-davinci-003 | Generates text based on prompt.")
    async def davinci3(self):
        """ /davinci3 """
        return
    
    @app_commands.command(name="curie", description="GPT-3 text-curie-001 | Less capable, but faster & cheaper.")
    async def curie(self):
        """ /curie """
        return

    @app_commands.command(name="babbage", description="GPT-3 text-babbage-001 | Straight-forward, faster & cheaper.")    
    async def babbage(self):
        """ /babbage """
        return
    
    @app_commands.command(name="ada", description="GPT-3 text-ada-001 | Very simple tasks, usually fastest, lowest cost.")
    async def ada(self):
        """ /ada """
        return

async def setup(bot: commands.Bot, auth, tkn ,org):
    await bot.add_cog(GPT3(bot, tkn, org))
