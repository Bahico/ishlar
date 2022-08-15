from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from bot.menu.main_menu import bot_main_menu
from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_corporation_add(message:types.Message,conn,callback_query):
    conn.execute("update I_ set settings = 'add corporation' where id = (?);",(message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id,"Yangi marka nomini kiriting")

async def bot_corporation_insert(message:types.Message,conn,vote_cb,bot_):
    conn.execute(f"insert into BRAND(name) values ('{message.text}');")
    await bot_main_menu(message,vote_cb,bot_[1],conn)
    conn.execute("update I_ set settings = NULL where id = (?);",(message.from_user.id,))