import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_start_admin(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData):
    person = conn.execute("select * from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
    if not person:
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row_width = 2
        markup.row(
            InlineKeyboardButton(text="🇺🇿 O'zbekcha",
                                 callback_data=vote_cb.new(stage="start", id="start", name="None", number="None",
                                                           language="uzb", action="branch")),
            InlineKeyboardButton(text="🇬🇧 English",
                                 callback_data=vote_cb.new(stage="start", id="start", name="None", number="None",
                                                           language="eng", action="branch")),
            InlineKeyboardButton(text="🇷🇺 Русский",
                                 callback_data=vote_cb.new(stage="start", id="start", name="None", number="None",
                                                           language="rus", action="branch"))
        )
        await bot.send_message(message.from_user.id, "Tilni tanlang 😊\nSelect a language 😊\nВыберите язык 😊",
                               reply_markup=markup)


async def admin_login(message: types.Message, conn: sqlite3.Connection, language: str):
    if language == "uzb":
        await bot.send_message(message.from_user.id, "Loginingizni kiriting:")
        conn.execute("insert into ADMIN(ID,SETTINGS,LANGUAGE) values (?,?,?);", (message.from_user.id, "login", "uzb"))
    elif language == "rus":
        await bot.send_message(message.from_user.id, "Введите ваш логин:")
        conn.execute("insert into ADMIN(ID,SETTINGS,LANGUAGE) values (?,?,?);", (message.from_user.id, "login", "rus"))
    elif language == "eng":
        await bot.send_message(message.from_user.id, "Enter your login:")
        conn.execute("insert into ADMIN(ID,SETTINGS,LANGUAGE) values (?,?,?);", (message.from_user.id, "login", "eng"))
