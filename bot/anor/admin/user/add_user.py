import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_user_category(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                              vote_cb: aiogram.utils.callback_data.CallbackData):
    category = main_conn.execute("select * from lessen_category;").fetchall()
    markup = InlineKeyboardMarkup(row_width=3)
    for i in category:
        markup.insert(
            InlineKeyboardButton(text=i[0],
                                 callback_data=vote_cb.new(rol='admin', stage="add user", stage1="category",
                                                           tur=i[1]))
        )
    await bot.send_message(message.from_user.id, "Yangi o'quvchi qaysi turda o'qidi?", reply_markup=markup)


async def admin_user_lessen(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                            vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    lessen = main_conn.execute("select * from lessen_fan where number = (?);", (callback_query["tur"],)).fetchall()
    markup = InlineKeyboardMarkup(row_width=3)
    for i in lessen:
        markup.insert(
            InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='admin', stage="add user", stage1="fan",
                                                                      tur=i[1]))
        )
    await bot.send_message(message.from_user.id, "Yangi o'quvchi qaysi fanda oq'idi?", reply_markup=markup)


async def admin_user_name(message: types.CallbackQuery, main_conn: sqlite3.Connection, callback_query: dict):
    main_conn.execute("update all_user set text = 'add user name', save = (?) where id = (?);",
                      (callback_query["tur"], message.from_user.id,))
    await bot.send_message(message.from_user.id, "Yangi o'quvchini ismi nima?")


async def admin_user_phone(message: types.Message, main_conn: sqlite3.Connection):
    admin = main_conn.execute("select save from all_user where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    main_conn.execute("""INSERT into users (number,username) values (?,?)""", (admin, message.text))
    id = main_conn.execute("""select id from users where number = (?) and username = (?)""",
                           (admin, message.text)).fetchall()[0][0]
    main_conn.execute("update all_user set text = 'add user phone number', save = (?) where id = (?);",
                      (id, message.from_user.id))
    await bot.send_message(message.from_user.id, "O'quvchining telefon raqamini yuboring\n\nMisol uchun: 950171208")


async def admin_user_add(message: types.Message, main_conn: sqlite3.Connection,
                         vote_cb: aiogram.utils.callback_data.CallbackData):
    admin = main_conn.execute("select save from all_user where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    main_conn.execute("update users set phone_number = (?) where id = (?);", (int(message.text), admin,))
    main_conn.execute("update all_user set text = null, save = null where id = (?);", (message.from_user.id,))
    await bot.send_message(message.from_user.id, "Yangi o'quvchi muofaqiyatli qo'shildi")
    await admin_menu(message, vote_cb)
