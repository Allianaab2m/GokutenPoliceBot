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
            error_embed = discord.Embed(title="エラー",
                                        description=f"すでに個人部屋を作成しているようです。",
                                        color=0xff0000)
            error_embed.set_footer(text="個人部屋を削除した場合にも，このメッセージが表示される場合があります。")
            await ctx.reply(embed=error_embed)

        else:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(manage_channels=False),
                ctx.author: discord.PermissionOverwrite(manage_channels=True)
            }
            await ctx.guild.create_text_channel(channel_name, category=category, overwrites=overwrites)
            ok_embed = discord.Embed(title="個人部屋作成",
                                     description=f"{channel_name}を作成しました。",
                                     color=0x51ff00)
            ok_embed.set_footer(text="自分で作成した個人部屋にのみ，チャンネルの編集権限が与えられています。チャンネルの名前の変更や削除を行えます。")
            await ctx.reply(embed=ok_embed)
            await ctx.author.add_roles(maked_role)


def setup(bot: Bot) -> None:
    bot.add_cog(Open(bot))
