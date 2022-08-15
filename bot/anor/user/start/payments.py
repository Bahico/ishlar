import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def user_payments_tur(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                            lessen_conn: sqlite3.Connection):
    lessen_type = lessen_conn.execute("select name, id from LESSEN_CATEGORY;").fetchall()
    if lessen_type:
        markup = InlineKeyboardMarkup()
        son = 0
        for i in lessen_type:
            son += 1
            if son >= 3:
                markup.insert(InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='user', stage="payments",
                                                                                        stage1="fan", tur=i[1])))
            else:
                son = 0
                markup.add(InlineKeyboardButton(text=i[0],
                                                callback_data=vote_cb.new(rol='user', stage="payments", stage1="fan",
                                                                          tur=i[1])))
        await bot.send_message(message.from_user.id, "pass", reply_markup=markup)
    else:
        markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text="⬅️ORTGA"))
        await bot.send_message(message.from_user.id, "Hozirda bizni darslar yo'q", reply_markup=markup)


async def user_payments_lessen(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                               lessen_conn: sqlite3.Connection, callback_query: dict):
    lessen_type = lessen_conn.execute("select name, id from lessen_fan where id = (?);", (callback_query["tur"])).fetchall()
    if lessen_type:
        markup = InlineKeyboardMarkup()
        son = 0
        for i in lessen_type:
            son += 1
            if son >= 3:
                markup.insert(InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='user', stage="payments",
                                                                                        stage1="fan", tur=i[1])))
            else:
                son = 0
                markup.add(InlineKeyboardButton(text=i[0],
                                                callback_data=vote_cb.new(rol='user', stage="payments", stage1="fan",
                                                                          tur=i[1])))
        await bot.send_message(message.from_user.id, "", reply_markup=markup)
    else:
        markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text="⬅️ORTGA"))
        await bot.send_message(message.from_user.id, "Hozirda bizni darslar yo'q", reply_markup=markup)


async def user_payments_fan(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData, lessen_conn: sqlite3.Connection, callback_query: dict):
    pass
