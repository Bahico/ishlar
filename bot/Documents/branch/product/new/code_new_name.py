import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from branch.menu.main_menu import admin_branch_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_add_car_name(message: types.Message, conn: sqlite3.Connection, language: str, vote_cb: aiogram.utils.callback_data.CallbackData):
    """

    :param message:
    :param conn:
    :param language:
    :param vote_cb:
    """
    try:
        await bot.delete_message(message.from_user.id, message.message_id - 1)
    except:
        pass
    add = message.text
    add = add.split(",")
    admin = conn.execute("select corporation from admin_ where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    conn.execute(
        f"insert into CAR(corporation,name) values ('{admin}','{add[0].strip()}');")
    conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))
    if language == "uzb":
        await bot.send_message(message.from_user.id, "Qabul qilindi✅")
    elif language == "rus":
        await bot.send_message(message.from_user.id, "Принятый✅")
    elif language == "eng":
        await bot.send_message(message.from_user.id, "Accepted✅")
    await admin_branch_menu(message, conn, vote_cb, language)
