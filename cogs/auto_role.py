from __future__ import annotations
from typing import TYPE_CHECKING

import discord

from ezcord import Cog
from constants import MEMBER_ROLE_ID

if TYPE_CHECKING:
    from bot import YoungDevsClubBot


class AutoRoleCog(Cog):
    def __init__(self, bot: YoungDevsClubBot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member: discord.Member):
        member_role = await member.guild._fetch_role(MEMBER_ROLE_ID)  # noqa

        if member_role is not None:
            await member.add_roles(member_role)


def setup(bot: YoungDevsClubBot):
    bot.add_cog(AutoRoleCog(bot))
