import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def user_course(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                      main_conn: sqlite3.Connection):
    lessen_type = main_conn.execute("select name, id from lessen_category;").fetchall()
    if lessen_type:
        markup = InlineKeyboardMarkup()
        son = 0
        for i in lessen_type:
            son += 1
            if son >= 3:
                markup.insert(InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='user', stage="start",
                                                                                        stage1="course", tur=i[1])))
            else:
                son = 0
                markup.add(InlineKeyboardButton(text=i[0],
                                                callback_data=vote_cb.new(rol='user', stage="start", stage1="course",
                                                                          tur=i[1])))
        await bot.send_message(message.from_user.id, "pass", reply_markup=markup)
    else:
        markup = InlineKeyboardMarkup(inline_keyboard=True).add(
            InlineKeyboardButton(text="⬅️ORTGA", callback_data=vote_cb.new(rol='user', stage="back",
                                                                           stage1="back", tur="")))
        await bot.send_message(message.from_user.id, "Hozirda bizni darslar yo'q", reply_markup=markup)


async def user_fan(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                   main_conn: sqlite3.Connection, callback_query: dict):
    lessen_type = main_conn.execute("select name, id from lessen_fan where id = (?);",
                                    (callback_query["tur"],)).fetchall()
    if lessen_type:
        markup = InlineKeyboardMarkup()
        son = 0
        for i in lessen_type:
            son += 1
            if son >= 3:
                markup.insert(InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='user', stage="start",
                                                                                        stage1="fan", tur=i[1])))
            else:
                son = 0
                markup.add(InlineKeyboardButton(text=i[0],
                                                callback_data=vote_cb.new(rol='user', stage="start", stage1="fan",
                                                                          tur=i[1])))
        await bot.send_message(message.from_user.id, "", reply_markup=markup)
    else:
        markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text="⬅️ORTGA"))
        await bot.send_message(message.from_user.id, "Hozirda bizni darslar yo'q", reply_markup=markup)


async def user_main_fan(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                        main_conn: sqlite3.Connection, callback_query: dict):
    lesson = main_conn.execute("select description, price, name from lessen_fan where id = (?);",
                               (callback_query["tur"],)).fetchall()[0]
    awa = "Fan: " + lesson[2] + "\nDescription: " + lesson[0] + "\nPrice: " + str(lesson[1]) + " so'm"
    markup = InlineKeyboardMarkup(reply_markup=True).add(
        InlineKeyboardButton(text="💳Payments",
                             callback_data=vote_cb.new(rol='user', stage='start', stage1="", tur="payments")),
    )
    await bot.send_message(message.from_user.id, awa, reply_markup=markup)
