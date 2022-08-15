import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_start(message: types.Message, main_conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData):
    admin = main_conn.execute("select text from all_user where id = (?);", (message.from_user.id,)).fetchall()
    if admin:
        if admin[0][0] == "password":
            await admin_password(message, main_conn, vote_cb)
        else:
            await admin_menu(message, vote_cb)
    else:
        main_conn.execute("insert into all_user(id,name,text, test) values (?,'admin', 'password', 0);",
                          (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Password: ")


async def admin_password(message: types.Message, main_conn: sqlite3.Connection,
                         vote_cb: aiogram.utils.callback_data.CallbackData):
    code = main_conn.execute("select code from code;").fetchall()[0][0]
    admin = main_conn.execute("select test from all_user where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    if message.text == code:
        main_conn.execute("update all_user set text = 'true' where id = (?);", (message.from_user.id,))
        await bot.send_message(message.from_user.id, "Qabul qilindi✅")
        await admin_menu(message, vote_cb)
    else:
        if admin >= 3:
            main_conn.execute("delete from all_user where id = (?);")
        else:
            main_conn.execute("update all_user set test = (?) where id = (?);", (admin + 1, message.from_user.id,))
        await bot.send_message(message.from_user.id, "Notog'ri❌")
