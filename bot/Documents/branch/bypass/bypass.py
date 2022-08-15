import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from branch.product.product_plus import admin_plus_brand
from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def branch_name_bypass(message: types.Message, conn: sqlite3.Connection,
                             vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """

    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    """
    admin = conn.execute("select corporation from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    car = conn.execute("select ID from CAR where corporation = (?) and name = 'bypass';", (admin,)).fetchall()
    if not car:
        conn.execute("insert into CAR(corporation,name) values (?,'bypass');", (admin,))
        car = conn.execute("select id from CAR where corporation = (?) and name = 'bypass';", (admin,)).fetchall()[0][0]
    else:
        car = car[0][0]
    callback_query["name"] = car
    await admin_plus_brand(message, conn, vote_cb, callback_query)
