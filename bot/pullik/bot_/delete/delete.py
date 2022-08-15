from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot_.number.user_number import get_user_number
from bot_.number.admin_number import get_admin_number

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_user_del(message: types.Message, conn, id, type, vote_cb):
    conn.execute(f"delete from {type} where id = (?);", (int(id)))
    if type == "client":
        await get_user_number(message,conn,vote_cb)
    else:
        await get_admin_number(message,conn,vote_cb)
