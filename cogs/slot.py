import random
import time

import discord
from discord.ext.commands import Bot, Cog, Context, command

from sheets import sheet


class Slot(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def slot(self, ctx: Context) -> None:
        """スロットを実行します。"""
        if ctx.channel.id != 868404450790891530:
            error_embed = discord.Embed(title="エラー",
                                        description="専用チャンネルで投稿してください。このメッセージは5秒後に削除されます。",
                                        color=0xff0000)
            error_mes = await ctx.reply(embed=error_embed)
            time.sleep(5)
            await ctx.message.delete()
            await error_mes.delete()
            return

        author_name = str(ctx.author)
        worksheet = sheet.sheet_setup('slotresult')  # sheet_setup関数でslotresultシートを指定
        name_cell = worksheet.find(author_name)  # すでに登録済かチェック

        if name_cell is None:  # 登録されていない場合
            datas = [author_name, 100]
            worksheet.append_row(datas)  # 新規登録
            name_cell = worksheet.find(author_name)
        else:
            pass
        point_cell_value = int(worksheet.cell(name_cell.row, name_cell.col+1).value)

        async def slot_sys() -> None:
            SLOT_STAT: list = ["🍐", "🫀", "🌚", "🍭", "💩"]
            slot_result: list = random.choices(SLOT_STAT, k=3)
            if slot_result[0] == slot_result[1] == slot_result[2]:
                cell_value: int = point_cell_value + 100
                result_embed = discord.Embed(title="当たり！",
                                             description=f"現在のポイント数:{cell_value}")
                await ctx.reply(embed=result_embed)
                worksheet.update_cell(name_cell.row, name_cell.col+1, f"{cell_value}")
            else:
                cell_value: int = point_cell_value - 10
                result_embed = discord.Embed(title="ハズレ",
                                             description=f"現在のポイント数:{cell_value}")
                await ctx.reply(embed=result_embed)
                worksheet.update_cell(name_cell.row, name_cell.col+1, f"{cell_value}")

        await slot_sys()


def setup(bot: Bot) -> None:
    bot.add_cog(Slot(bot))
