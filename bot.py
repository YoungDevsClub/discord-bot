import discord
import os

from ezcord import Bot
from dotenv import load_dotenv

load_dotenv()


class YoungDevsClubBot(Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        debug_guilds = [os.getenv("GUILD_ID")]

        super().__init__(
            intents=intents,
            debug_guilds=debug_guilds,
            error_handler=False  # Using a custom error handler instead of ezcord's built-in one
        )

        self.load_cogs()
