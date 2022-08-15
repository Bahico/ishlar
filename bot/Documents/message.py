import sqlite3
import typing

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot.message import bot_message
from branch.message.message import branch_message
from client.message.message import client_message

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_message_all(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData):
    admin = conn.execute("select settings, branch, test from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
    client = conn.execute("select * from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    bot_ = conn.execute("select settings, language, name, login from I_ where id = (?);",
                        (message.from_user.id,)).fetchall()
    if bot_:
        await bot_message(message, conn, vote_cb, bot_[0])
    elif admin:
        await branch_message(message, conn, vote_cb)
    elif client:
        await client_message(message, conn, vote_cb)
    conn.commit()
