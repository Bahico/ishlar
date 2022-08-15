import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_payment_category(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                                 vote_cb: aiogram.utils.callback_data.CallbackData):
    category = main_conn.execute("select name, id from lessen_category;").fetchall()
    markup = InlineKeyboardMarkup()
    for i in category:
        markup.insert(
            InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='admin', stage="payment", stage1="category",
                                                                      tur=i[1])))
    await bot.send_message(message.from_user.id, "Qaysi tuda o'qidi", reply_markup=markup)


async def admin_payment_fan(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                            vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    category = main_conn.execute("select name, id from lessen_fan where number = (?);",
                                 (callback_query["tur"],)).fetchall()
    markup = InlineKeyboardMarkup()
    for i in category:
        markup.insert(
            InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='admin', stage="payment", stage1="fan",
                                                                      tur=i[1])))
    await bot.send_message(message.from_user.id, "Qaysi fanda o'qidi", reply_markup=markup)


async def admin_payment_user(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                             vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    category = main_conn.execute("select username, id from users where number = (?);",
                                 (callback_query["tur"],)).fetchall()
    markup = InlineKeyboardMarkup()
    for i in category:
        markup.insert(
            InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='admin', stage="payment", stage1="student",
                                                                      tur=i[1])))
    await bot.send_message(message.from_user.id, "Qaysi o'quvchi tolov qildi", reply_markup=markup)


async def admin_payment_price(message: types.CallbackQuery, main_conn: sqlite3.Connection, callback_query: dict):
    main_conn.execute("update all_user set save = (?), text = 'payment money' where id = (?);",
                      (callback_query["tur"], message.from_user.id))
    await bot.send_message(message.from_user.id, "Qancha to'lov qildi?")


async def admin_payment_date(message: types.Message, main_conn: sqlite3.Connection):
    main_conn.execute("update all_user set test = (?) where id = (?);", (int(message.text), message.from_user.id))
    main_conn.execute("update all_user set text = 'payment date' where id = (?);", (message.from_user.id,))
    await message.answer("Qachon to'lo'v qilganini kiriting\nMisol uchun: oy/kun/yil➡️12/31/22")


async def admin_payment_finish(message: types.Message, main_conn: sqlite3.Connection,
                               vote_cb: aiogram.utils.callback_data.CallbackData):
    if len(message.text) == 7:
        text = message.text
        if text[2] == "/" and text[5] == "/":
            admin = \
                main_conn.execute("select save, test from all_user where id = (?);",
                                  (message.from_user.id,)).fetchall()[0]
            main_conn.execute("insert into payment(id, price, date) VALUES (?,?,?);",
                              (admin[0], admin[1], message.text))
            main_conn.execute("update all_user set text = null, test = null, save = null where id = (?);", (message.from_user.id,))
            await message.answer("Tolov qabul qilindi")
            await admin_menu(message, vote_cb)
        else:
            await message.answer("Iltimos togri yuboring\nMisol uchun: oy/kun/yil➡️12/31/22")
    else:
        await message.answer("Iltimos togri yuboring\nMisol uchun: oy/kun/yil➡️12/31/22")
