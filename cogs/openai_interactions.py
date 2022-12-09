# xzavyer.dev
import discord
import aiohttp
from discord import app_commands
from discord.ext import commands
from typing import Optional

class GPT3(commands.GroupCog, name="gpt3", group_description="Generates text based content based on a prompt using AI."):
    def __init__(self, bot: commands.Bot, auth: str, tkn: int, org: str):
        self.bot = bot
        self.client = aiohttp.ClientSession()
        self.headers = {"Authorization": "Bearer " + auth}
        if org != "default":
            self.headers.update({"OpenAI-Organization": org})
        self.max = tkn
        self.org = org

        super().__init__()

    @app_commands.command(name="davinci", description="GPT-3 text-davinci-003 | Generates text based on prompt.")
    @app_commands.describe(prompt="Prompt",
                            maxLen="Max # of tokens to use for this request.",
                            temp="(Decimal between 0-1) Controls randomness.")
    async def davinci3(self, prompt: str, maxLen: Optional[int], temp: Optional[float]):
        """ /davinci3 """
        return
    
    @app_commands.command(name="curie", description="GPT-3 text-curie-001 | Less capable, but faster & cheaper.")
    @app_commands.describe(prompt="Prompt",
                            maxLen="Max # of tokens to use for this request.",
                            temp="(Decimal between 0-1) Controls randomness.")
    async def curie(self):
        """ /curie """
        return

    @app_commands.command(name="babbage", description="GPT-3 text-babbage-001 | Straight-forward, faster & cheaper.")    
    @app_commands.describe(prompt="Prompt",
                            maxLen="Max # of tokens to use for this request.",
                            temp="(Decimal between 0-1) Controls randomness.")
    async def babbage(self):
        """ /babbage """
        return
    
    @app_commands.command(name="ada", description="GPT-3 text-ada-001 | Very simple tasks, usually fastest, lowest cost.")
    @app_commands.describe(prompt="Prompt",
                            maxLen="Max # of tokens to use for this request.",
                            temp="(Decimal between 0-1) Controls randomness.")
    async def ada(self):
        """ /ada """
        return

async def setup(bot: commands.Bot, auth, tkn ,org):
    await bot.add_cog(GPT3(bot, tkn, org))
