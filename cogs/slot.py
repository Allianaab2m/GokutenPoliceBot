import random

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
            SLOT_STAT: list = ["1", "2", "3", "4", "5"]
            slot_result: list = random.choices(SLOT_STAT, k=3)
            if slot_result[0] == slot_result[1] == slot_result[2]:
                cell_value: int = point_cell_value + 100
                await ctx.reply(f"{slot_result}\n当たり！現在のポイント数:{cell_value}")
                worksheet.update_cell(name_cell.row, name_cell.col+1, f"{cell_value}")
            else:
                cell_value: int = point_cell_value - 10
                await ctx.reply(f"{slot_result}\nハズレ 現在のポイント数:{cell_value}")
                worksheet.update_cell(name_cell.row, name_cell.col+1, f"{cell_value}")

        await slot_sys()


def setup(bot: Bot) -> None:
    bot.add_cog(Slot(bot))
