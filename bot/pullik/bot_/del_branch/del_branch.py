from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_del_branch(message: types.Message, conn, vote_cb):
    branch = conn.execute("select id, name from BRANCH;").fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    for i in branch:
        markup.add(InlineKeyboardButton(text=i[1], callback_data=vote_cb.new(location="branch", text="del", branch=i[0],
                                                                             language="uzb", action="bot_")))
    await bot.send_message(message.from_user.id, "Qaysi filialni o'chirish kerak.", reply_markup=markup)


async def get_delete(message: types.Message, conn, id):
    conn.execute("delete from BRANCH where id = (?);", (id,))
    await bot.send_message(message.from_user.id, "O'chirildi✅")
