import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_lessen_category(message: types.CallbackQuery, vote_cb: aiogram.utils.callback_data.CallbackData,
                                main_conn: sqlite3.Connection):
    category = main_conn.execute("select * from lessen_category;").fetchall()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in category:
        markup.insert(
            InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(rol='admin', stage="lessen", stage1="category",
                                                                      tur=i[1])))
    markup.insert(
        InlineKeyboardButton(text="⬅️ORTGA", callback_data=vote_cb.new(rol='admin', stage="back", stage1="back",
                                                                       tur="")))
    await bot.send_message(message.from_user.id, "Qaysi Kategoryaga fan qo'shmoqchisiz?", reply_markup=markup)


async def admin_lessen_fan(message: types.CallbackQuery, vote_cb: aiogram.utils.callback_data.CallbackData,
                           main_conn: sqlite3.Connection, callback_query: dict):
    main_conn.execute("update all_user set save = (?), text = 'add fan name' where id = (?);",
                      (callback_query["tur"], message.from_user.id))
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="⬅️ORTGA", callback_data=vote_cb.new(rol='admin', stage="back", stage1="save",
                                                                       tur=""))
    )
    await bot.send_message(message.from_user.id, "Yangi fan nomini kiriting", reply_markup=markup)


async def admin_lessen_description(message: types.Message, main_conn: sqlite3.Connection):
    admin = main_conn.execute("select save from all_user where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    main_conn.execute(f"insert into lessen_fan(name, number) VALUES ('{message.text}',?);", (admin,))
    number = \
        main_conn.execute(f"select id from lessen_fan where name = '{message.text}' and number = {admin};").fetchall()[
            0][0]
    main_conn.execute("update all_user set save = (?), text = 'add fan price' where id = (?);",
                      (number, message.from_user.id,))
    await bot.send_message(message.from_user.id, "Fan narxini kiriting")


async def admin_lesson_finish(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                              main_conn: sqlite3.Connection):
    admin = main_conn.execute("select save from all_user where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    main_conn.execute("""update lessen_fan set price = (?) where id = (?);""", (message.text, admin))
    await bot.send_message(message.from_user.id, "Qabul qilindi✅")
    await admin_menu(message, vote_cb)
    main_conn.execute("update all_user set text = null where id = (?);", (message.from_user.id,))
