import sqlite3

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_bot_code_edit(message: types.Message, conn: sqlite3.Connection, callback_query: dict):
    conn.execute("update I_ set settings = 'bot_code_edit' where id = (?);", (message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "O'zgartiriladigan kodni kirting.")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Введите код для изменения.")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Enter the code to change.")
