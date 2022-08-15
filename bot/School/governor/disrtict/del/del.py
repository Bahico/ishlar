from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def governor_district_del(message:types.Message,district_conn,vote_cb):
    district = district_conn.execute("select name, id from CONN;").fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    for i in district:
        markup.insert(
            InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(name="del",province="delete",city=i[1],school="",tur="None",clas="None",action="governor"))
        )
