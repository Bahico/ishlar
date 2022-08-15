import sqlite3

import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_car_corporation(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """
    O'chiriladigan extiyot qismning mashina turlari
    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return: car arr
    """
    car = conn.execute("select name, id from brand").fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car:
        markup.insert(InlineKeyboardButton(text=i[0],
                                           callback_data=vote_cb.new(stage="corporation", id="del_menu", name=i[1],
                                                                     number="None", language=callback_query["language"],
                                                                     action="bot")))

    if callback_query["language"] == "uzb":
        markup.insert(InlineKeyboardButton(text="Hammasi❌",
                                           callback_data=vote_cb.new(stage="corporation", id="del_menu", name="all",
                                                                     number="None", language=callback_query["language"],
                                                                     action="bot")))
        markup.insert(InlineKeyboardButton(text="⬅️Ortga",
                                           callback_data=vote_cb.new(stage="corporation", id="del_menu", name="back",
                                                                     number="None", language=callback_query["language"],
                                                                     action="bot")))
        await bot.send_message(message.from_user.id, "Qaysi turdagi mashinaning extiyot qisimi kerak",
                               reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.insert(InlineKeyboardButton(text="Hammasi❌",
                                           callback_data=vote_cb.new(stage="corporation", id="del_menu", name="all",
                                                                     number="None", language=callback_query["language"],
                                                                     action="bot")))
        markup.insert(InlineKeyboardButton(text="⬅️Ortga",
                                           callback_data=vote_cb.new(stage="corporation", id="del_menu", name="back",
                                                                     number="None", language=callback_query["language"],
                                                                     action="bot")))
        await bot.send_message(message.from_user.id, "Qaysi turdagi mashinaning extiyot qisimi kerak",
                               reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.insert(InlineKeyboardButton(text="Hammasi❌",
                                           callback_data=vote_cb.new(stage="corporation", id="del_menu", name="all",
                                                                     number="None", language=callback_query["language"],
                                                                     action="bot")))
        markup.insert(InlineKeyboardButton(text="⬅️Ortga",
                                           callback_data=vote_cb.new(stage="corporation", id="del_menu", name="back",
                                                                     number="None", language=callback_query["language"],
                                                                     action="bot")))
        await bot.send_message(message.from_user.id, "Qaysi turdagi mashinaning extiyot qisimi kerak",
                               reply_markup=markup)


async def bot_del_all_corporation(message: types.Message, conn: sqlite3.Connection):
    conn.execute("delete from SPARE;")
    conn.execute("delete from CAR;")
    conn.execute("delete from BRANCH_SPARE;")
    conn.execute("delete from ADMIN_;")
    conn.execute("delete from CLIENT_;")
    await bot.send_message(message.from_user.id, "CLear")
