from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_admin_main(message:types.Message,conn,vote_cb,callback_query):
    if callback_query["language"] == "uzb":
        admin = conn.execute("select * from ADMIN where branch = (?);",(callback_query["number"],)).fetchall()
