import sys
sys.path.append("..")
import const

import discord
from discord.ext.commands import Bot, Cog, Context, command
from discord import Message


class No_report(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener(name='on_message')
    async def no_report(self, message: Message):
        if message.author.bot:
            return
        if const.NG_WORD in message.content:
            await message.delete()


def setup(bot: Bot) -> None:
    bot.add_cog(No_report(bot))
