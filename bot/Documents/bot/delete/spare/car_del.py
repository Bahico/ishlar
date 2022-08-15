import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.menu.main_menu import bot_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_car_del(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    conn.execute("delete from CAR where id  = (?);", (callback_query["name"],))
    conn.execute("delete from SPARE where id = (?);", (callback_query["name"],))
    conn.execute("delete from BRANCH_SPARE where id = (?);", (callback_query["name"],))
    conn.execute("delete from ADMIN_ where spare = (?);", (callback_query["name"],))
    conn.execute("update CLIENT_ set spare = Null where spare = (?);", (callback_query["name"],))
    await bot_main_menu(message, vote_cb, callback_query["language"], conn)
