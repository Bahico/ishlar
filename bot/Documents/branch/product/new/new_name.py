import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_new_name(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, language: str):
    """
    Yangi mashina qo'shishga start beradi
    :param language:
    :param message:
    :param conn:
    :param vote_cb:
    :return:
    """
    conn.execute("update ADMIN set settings = 'add_name' where id = (?);", (message.from_user.id,)).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True).row(
        InlineKeyboardButton(text="STOP",
                             callback_data=vote_cb.new(stage="stop", id="car_plus", name="None", number="None",
                                                       language=language, action="branch"))
    )
    if language == "uzb":
        await bot.send_message(message.from_user.id,
                               "Yangi mashinaning nomini kiriting \n\nYoki adashgan bo'lsangiz \"STOP\" tugmasini bosing",
                               reply_markup=markup)
    elif language == "rus":
        await bot.send_message(message.from_user.id,
                               "Если вы хотите добавить новый автомобиль, введите его следующим образом: марка,модель,позиция,год изготовления\n\nИли \"СТОП\", если вы сбиваетесь с пути",
                               reply_markup=markup)
    elif language == "eng":
        await bot.send_message(message.from_user.id,
                               "If you want to add a new car, enter it as follows: brand,model,position,year of manufacture\n\nOr \"STOP\" if you are go astray",
                               reply_markup=markup)
