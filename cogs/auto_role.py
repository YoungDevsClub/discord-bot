from __future__ import annotations
from typing import TYPE_CHECKING

import discord

from ezcord import Cog
from constants import MEMBER_ROLE_ID, BOT_ROLE_ID

if TYPE_CHECKING:
    from bot import YoungDevsClubBot


class AutoRoleCog(Cog):
    def __init__(self, bot: YoungDevsClubBot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member: discord.Member):
        role_id = MEMBER_ROLE_ID if not member.bot else BOT_ROLE_ID
        member_role = await self._get_role(member.guild, role_id)

        if member_role is not None:
            await member.add_roles(member_role)

    @staticmethod
    async def _get_role(guild: discord.Guild, role_id: int) -> discord.Role:
        return await guild._fetch_role(role_id)  # noqa


def setup(bot: YoungDevsClubBot):
    bot.add_cog(AutoRoleCog(bot))
