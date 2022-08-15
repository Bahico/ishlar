import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from branch.menu.main_menu import admin_branch_menu
from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def branch_oil_menu(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row(
        InlineKeyboardButton(text="+", callback_data=vote_cb.new(stage="+", id="oil", name="", number="",
                                                                 language=callback_query["language"], action="branch")),
        InlineKeyboardButton(text="-", callback_data=vote_cb.new(stage="-", id="oil", name="", number="",
                                                                 language=callback_query["language"], action="branch"))
    )
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Mashina yog'i qo'shasizmi yoki o'chirasizmi?",
                               reply_markup=markup)


async def branch_oil_type(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    markup = InlineKeyboardMarkup(reply_markup=True)
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="Mator moyi",
                                 callback_data=vote_cb.new(stage="type", id="oil", name="mator", number="",
                                                           language=callback_query["language"], action="branch")),
            InlineKeyboardButton(text="Karobka moyi",
                                 callback_data=vote_cb.new(stage="type", id="oil", name="karobka", number="",
                                                           language=callback_query["language"], action="branch"))
        )
        await bot.send_message(message.from_user.id, "Qaysi turdagi moydan kerak?", reply_markup=markup)


async def branch_oil_arr(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    oil = conn.execute(f"select name, id from OIL where type = '{callback_query['name']}';").fetchall()
    markup = InlineKeyboardMarkup(reply_markup=True)
    markup.row_width = 3
    for i in oil:
        markup.insert(InlineKeyboardButton(text=i[0],
                                           callback_data=vote_cb.new(stage="oil", id="oil", name=i[1], number="",
                                                                     language=callback_query["language"],
                                                                     action="branch")))
    if callback_query["language"] == "uzb":
        markup.add(InlineKeyboardButton(text="Yangi qo'shish",
                                        callback_data=vote_cb.new(stage="oil", id="oil", name="new", number="",
                                                                  language=callback_query["language"],
                                                                  action="branch")))
        if oil:
            await bot.send_message(message.from_user.id, "Qaysi maxsulotdan qo'shmoqchisiz\n\nYoki yangimi",
                                   reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id, "Yangi maxsulotni nomini yo'zing")
            conn.execute(
                "update ADMIN set settings = 'add oil' where id = (?);", (message.from_user.id,))
    admin = conn.execute("select * from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()
    if admin:
        conn.execute(
            f"update ADMIN_ set corporation = Null, name = Null, number = Null, paditsiya = Null, spare = Null, tur = '{callback_query['name']}' where id = (?);",
            (message.from_user.id,))
    else:
        conn.execute("insert into ADMIN_(id,tur) values (?,?);", (message.from_user.id, callback_query["name"]))


async def branch_oil_button_add(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    spare = conn.execute("select branches from OIL where id = (?);", (callback_query["name"],)).fetchall()[0]
    admin = conn.execute("select branch from ADMIN where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    son = 0
    admin = str(admin)
    for i in spare[0].splti("."):
        if i.split(",")[0] == admin:
            son = 1
            break
    if callback_query["language"] == "uzb":
        if son == 0:
            await bot.send_message(message.from_user.id, "Maxsulotni narxini kiriting")
            conn.execute(f"update ADMIN set settings = 'add oil many' where id = (?);", (message.from_user.id,))
            conn.execute("update ADMIN_ set spare = (?) where id = (?);",
                         (callback_query["name"], message.from_user.id))
        else:
            await bot.send_message(message.from_user.id, "Bu maxsulot oldin ham qo'shilgan"); await admin_branch_menu(
                message, conn, vote_cb, callback_query["language"])


async def branch_oil_add_many(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, admin: list):
    await message.answer("✅✅")
    spare = conn.execute("select spare from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    spare_ = conn.execute("select branches from OIL where id = (?);", (spare,)).fetchall()[0][0]
    conn.execute(f"update OIL set branches = '{spare_}.{admin[1]},{message.text}' where id = (?);", (spare,))
    await admin_branch_menu(message, conn, vote_cb, admin[3])
    await bot.delete_message(message.from_user.id, message.message_id + 1)


async def branch_oil_button(message: types.Message, conn: sqlite3.Connection, callback_query: dict):
    conn.execute("update ADMIN set settings = 'add spare name' where id = (?);", (message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Maxsulotni nomini kiriting")


async def branch_oil_name(message: types.Message, conn: sqlite3.Connection, admin: list):
    language = admin[3]
    admin = conn.execute("select tur from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    spare = conn.execute(f"select id from OIL where tur = '{admin[0]}' and name = '{message.text}';").fetchall()
    if spare:
        conn.execute("update ADMIN_ set spare = (?), tur = NULL where id = (?);", (spare[0][0], message.from_user.id))
    else:
        conn.execute(f"update ADMIN_ set name = '{message.text}' where id = (?);", (message.from_user.id,))
    conn.execute("update ADMIN set settings = 'oil many' where id = (?);", (message.from_user.id,))

    if language == "uzb":
        await bot.send_message(message.from_user.id, "Maxsulotni narxini kiriting")


async def branch_oil_many(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, admin: list):
    admin_ = conn.execute("select name, spare, tur from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    if admin_[2] is None:
        spare = conn.execute("select branches from OIL where id = (?);", (admin_[1],)).fetchall()[0][0]
        conn.execute(f"update OIL set branches = '{spare}.{admin[1]},{message.text}' where id = (?);", (admin_[1],))
    else:
        conn.execute("insert into OIL(name,branches,type) values (?,?,?);",
                     (admin_[0], str(admin[1]) + "," + message.text, admin_[2]))
    conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))
    if admin[3] == "uzb":
        await bot.send_message(message.from_user.id, "Maxsulot qo'shildi")

    await admin_branch_menu(message, conn, vote_cb, admin[3])
