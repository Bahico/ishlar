import sqlite3

import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.message import admin_message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def user_start(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                     main_conn: sqlite3.Connection):
    try:
        await message.delete()
    except:
        pass
    user = main_conn.execute("select name from ALL_USER where id = (?);", (message.from_user.id,)).fetchall()
    if not user or user[0][0] == "user":
        markup = InlineKeyboardMarkup().row(
            InlineKeyboardButton(text="💳Payments",
                                 callback_data=vote_cb.new(rol='user', stage='start', stage1="", tur="payments")),
            InlineKeyboardButton(text="💬About",
                                 callback_data=vote_cb.new(rol='user', stage='start', stage1="", tur="about")),
            InlineKeyboardButton(text="📚Courses",
                                 callback_data=vote_cb.new(rol="user", stage='start', stage1="", tur="courses"))
        )
        await bot.send_message(message.from_user.id, "👋Salom Bizning botimizga hush kelibsiz", reply_markup=markup)
    elif user[0][0] == "admin":
        await admin_message(message, vote_cb, main_conn)
