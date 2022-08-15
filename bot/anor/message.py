import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.message import admin_message
from config import TOKEN
from user.start.start import user_start

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def main_message(message: types.Message, main_conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData):
    user = main_conn.execute("select name from all_user where id = (?);", (message.from_user.id,)).fetchall()
    if user and user[0][0] == "admin":
        await admin_message(message, vote_cb, main_conn)
    elif not user:
        await user_start(message, vote_cb, main_conn)
