import sqlite3

import aiogram.utils.callback_data
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from admin.menu import admin_menu
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_user_pagination(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                                vote_cb: aiogram.utils.callback_data.CallbackData,
                                callback_query: dict):
    students = main_conn.execute("select username, id from users limit (?);", (int(callback_query["tur"]),)).fetchall()[
               int(callback_query["tur"]) - 10:]
    markup = InlineKeyboardMarkup(row_width=2)
    if not students:
        students = main_conn.execute("select username, id from users limit 10;", ).fetchall()
        markup.row(
            InlineKeyboardButton(text="➡️", callback_data=vote_cb.new(rol='admin', stage="user", stage1="pagination",
                                                                      tur=10)),
        )
    else:
        if callback_query["tur"] != 10:
            markup.row(
                InlineKeyboardButton(text="⬅️",
                                     callback_data=vote_cb.new(rol='admin', stage="user", stage1="pagination",
                                                               tur=int(callback_query["tur"]) - 10)),
                InlineKeyboardButton(text="➡️",
                                     callback_data=vote_cb.new(rol='admin', stage="user", stage1="pagination",
                                                               tur=int(callback_query["tur"]) + 10)),
            )
        else:
            markup.row(
                InlineKeyboardButton(text="➡️",
                                     callback_data=vote_cb.new(rol='admin', stage="user", stage1="pagination",
                                                               tur=int(callback_query["tur"]) + 10)),
            )
    if not students:
        try:
            await bot.edit_message_text("Hozircha o'quvchilar yo'q", message.from_user.id, message.message.message_id)
        except:
            await bot.send_message(message.from_user.id, "Hozircha o'quvchilar yo'q")
        await admin_menu(message, vote_cb)
    else:
        for i in students:
            markup.insert(
                InlineKeyboardButton(text=i[0],
                                     callback_data=vote_cb.new(rol='admin', stage="user", stage1="information",
                                                               tur=i[1])))
        try:
            await bot.edit_message_text("Qaysi o'quvchini malumotlarini kormoqchisiz", message.from_user.id,
                                        message.message.message_id, reply_markup=markup)
        except:
            await bot.send_message(message.from_user.id, "Qaysi o'quvchini malumotlarini kormoqchisiz",
                                   reply_markup=markup)


async def admin_user_information(message: types.CallbackQuery, main_conn: sqlite3.Connection,
                                 vote_cb: aiogram.utils.callback_data.CallbackData,
                                 callback_query: dict):
    student = main_conn.execute("select id, username, phone_number, number from users where id = (?);",
                                (callback_query["tur"],)).fetchall()[0]
    fan = main_conn.execute("select name, id from lessen_fan where id = (?);", (student[3],)).fetchall()[0]
    category = main_conn.execute("select name from lessen_category where id = (?);", (fan[1],)).fetchall()[0][0]
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="❌DELETE", callback_data=vote_cb.new(rol='admin', stage="user", stage1="delete",
                                                                       tur=student[0])))
    await bot.send_message(message.from_user.id,
                           f"""ID: {student[0]}\nO'qish turi: {category}\nO'qiydigon fani: {fan[0]}\nNomi: {student[1]}\nTelefon raqami: +998{student[2]}""", reply_markup=markup)
    await admin_menu(message, vote_cb)


async def admin_user_delete(main_conn: sqlite3.Connection, id: int):
    main_conn.execute("delete from users where id = (?);", (id,))
