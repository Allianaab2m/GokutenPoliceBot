from discord.ext.commands import Bot, CheckFailure, Cog, CommandError, CommandNotFound, Context, \
    errors
import discord


class CommandErrorHandler(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError) -> None:
        ignore_errors = (CheckFailure, CommandNotFound)
        if isinstance(error, ignore_errors):
            return
        error_embed: discord.Embed = discord.Embed(title="エラー",
                                                   description="エラーが発生しました。\n"
                                                               "このエラーが複数回発生する場合は，直るまで気長に待ってください。",
                                                   color=0xff0000)
        error_embed.add_field(name="エラー内容", value=str(error))
        await ctx.reply(embed=error_embed)


def setup(bot: Bot) -> None:
    bot.add_cog(CommandErrorHandler(bot))
