import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_edit_name(message: types.Message, conn: sqlite3.Connection,
                          vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    Foydalanuvchining filialining yangi nomini soraydi
    :param vote_cb:
    :param message:
    :param conn:
    :param callback_query:
    :return: user ga response beradi
    """
    conn.execute("update ADMIN set settings = 'edit_name' where id = (?);", (message.from_user.id,))
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(
        InlineKeyboardButton(text="STOP",
                             callback_data=vote_cb.new(stage="stop", id="car_plus", name="None",
                                                       number=callback_query["number"],
                                                       language=callback_query["language"], action="branch"))
    )
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Filialning yangi nomini kiriting.")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Введите новое название филиала.")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Enter the new name of the branch.")


async def admin_edit_branch(message: types.Message, conn: sqlite3.Connection, admin: list):
    """
    Foydalanuvchidan o'z filialining yangi nomini oladi
    :param message:
    :param conn:
    :param admin:
    :return: request oladi
    """
    conn.execute(f"update BRANCH set name = '{message.text}' where id = (?);", (admin[1],))
    if admin[3] == "uzb":
        await bot.send_message(message.from_user.id, f"Sizning filialingizni nomi {message.text} ga o'zgardi.")
    elif admin[3] == "rus":
        await bot.send_message(message.from_user.id, f"Название вашей ветки было изменено на {message.text}.")
    elif admin[3] == "eng":
        await bot.send_message(message.from_user.id, f"The name of your branch was changed to {message.text}.")
