import discord
from discord.ext.commands import Bot, Cog, Context, command


class Open(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def open(self, ctx: Context, name=None) -> None:
        """個人部屋を作成します。引数に部屋名を入れると，その名前で部屋を作成します。
        引数がなければ，〇〇の部屋として作成します。作成出来るチャンネルは１人１つまでです。
        """
        category = discord.utils.get(ctx.guild.categories, name="個人部屋")
        maked_role = discord.utils.get(ctx.guild.roles, name="個人部屋作成済")

        if name is None:
            channel_name: str = f"{ctx.author.name}の部屋"
        else:
            channel_name = name
        if maked_role in ctx.author.roles:
            await ctx.reply(f"すでに個人部屋を作成しているようです。")
        else:
            await ctx.guild.create_text_channel(channel_name, category=category)
            await ctx.reply(f"{channel_name}を作成しました。")
            await ctx.author.add_roles(maked_role)


def setup(bot: Bot) -> None:
    bot.add_cog(Open(bot))
