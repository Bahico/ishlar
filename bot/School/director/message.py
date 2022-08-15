from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code
from director.admin.add import director_admin_code, director_admin_insert

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def director_message(message:types.Message,director_conn,admin_conn,conn,vote_cb,director):
    if director[1] == "add admin login":
        await director_admin_code(message,director_conn, conn, vote_cb)
    elif director[1] == "add admin code":
        await director_admin_insert(message, director_conn, admin_conn, conn, vote_cb)