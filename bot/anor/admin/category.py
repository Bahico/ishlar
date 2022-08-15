import sqlite3

import aiogram
from aiogram import Bot, Dispatcher, types

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_category(message: types.CallbackQuery, main_conn: sqlite3.Connection):
    main_conn.execute("update all_user set text = 'add category' where id = (?);", (message.from_user.id,))
    await bot.send_message(message.from_user.id, "Yangi kategoryani kiriting")


async def admin_add_category(message:types.Message, vote_cb: aiogram.utils.callback_data.CallbackData, main_conn: sqlite3.Connection):
    main_conn.execute(f"insert into lessen_category(name) values ('{message.text}');")
    await bot.send_message(message.from_user.id, "Qabul qilindi")
    await admin_menu(message, vote_cb)
    main_conn.execute("update all_user set text = null where id = (?);", (message.from_user.id,))

