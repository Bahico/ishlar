import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_code_edit_call(message: types.CallbackQuery, main_conn: sqlite3.Connection):
    main_conn.execute("update all_user set text = 'edit code' where id = (?);", (message.from_user.id,))
    await bot.send_message(message.from_user.id, "Yangi kodni kiriting")


async def admin_code_edit_mes(message: types.Message, main_conn: sqlite3.Connection,
                              vote_cb: aiogram.utils.callback_data.CallbackData):
    main_conn.execute("""update code set code = (?);""", (message.text,))
    main_conn.execute("update all_user set text = null where id = (?);", (message.from_user.id,))
    await bot.send_message(message.from_user.id, "Qabul qilindi")
    await admin_menu(message, vote_cb)
