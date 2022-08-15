import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot.delete.spare.spare_type import bot_del_type

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_del_del(message: types.Message, conn: sqlite3.Connection,
                      vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    Extiyot qismni butunlay o'chrish
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: qayta menuni chiqarib beradi
    """

    car = conn.execute("select id from SPARE where number = (?);", (callback_query["name"],)).fetchall()[0]
    conn.execute("delete from SPARE where number = (?);", (callback_query["name"],))
    conn.execute("delete from BRANCH_SPARE where id = (?);", (callback_query["name"],))
    conn.execute("delete from ADMIN_ where spare = (?);", (callback_query["name"],))
    conn.execute("update CLIENT_ set spare = NULL where spare = (?);", (callback_query["name"],))
    callback_query["name"] = car[0]
    await bot_del_type(message, vote_cb, callback_query)
