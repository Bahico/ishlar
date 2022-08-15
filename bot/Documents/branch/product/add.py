import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_add(message: types.Message, conn: sqlite3.Connection, admin: list, type_: str):
    """
    Admindan yangi extiyot qism qabul qiladi
    :param type_:
    :param admin:
    :param message:
    :param conn:
    :return: yangi malumot qo'shadi
    """
    add = 0
    if type_ == "name":
        conn.execute(f"update ADMIN_ set name = '{message.text}' where id = (?);", (message.from_user.id,))
        conn.execute("update ADMIN set settings = 'add_spare many' where id = (?);", (message.from_user.id,))
    else:
        add = 1
        admin_ = \
        conn.execute("select name, spare, tur from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()[0]
        name = conn.execute(
            f"select id, branches from SPARE where id = (?) and tur = '{admin_[2]}' and spare_name = '{admin_[0]}';",
            (admin_[1],)).fetchall()
        if name:
            add = message.text
            conn.execute(
                f"update SPARE set branches = '{name[1] + '.' + admin[2] + ',' + add.strip()}' where number = (?);",
                (name[0],))

    if admin[3] == "uzb":
        if add == 1:
            await bot.send_message(message.from_user.id, "Qo'shildi✅")
            conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))
        else:
            await bot.send_message(message.from_user.id, "Maxsulot narxini yuboring")
            conn.execute("update ADMIN set settings = 'add_spare many' where id = (?);", (message.from_user.id,))
    elif admin[3] == "eng":
        if add == 1:
            await bot.send_message(message.from_user.id, "Added✅")
            conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))
        else:
            conn.execute("update ADMIN set settings = 'add_spare many' where id = (?);", (message.from_user.id,))
    elif admin[3] == "rus":
        if add == 1:
            await bot.send_message(message.from_user.id, "Добавлено✅")
            conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))
        else:
            conn.execute("update ADMIN set settings = 'add_spare many' where id = (?);", (message.from_user.id,))


async def admin_add_callback(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, callback_query: dict):
    """

    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    """
    admin = conn.execute("select spare from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    spare = conn.execute(f"select spare_name, number from SPARE where id = (?) and tur = '{callback_query['stage']}';",
                         (admin[0],)).fetchall()
    son = 0
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    for i in spare:
        son = 1
        markup.add(InlineKeyboardButton(text=i[0].split("[")[0],
                                        callback_data=vote_cb.new(stage=callback_query["stage"], id="spare_+",
                                                                  name=i[1], number="None",
                                                                  language=callback_query["language"],
                                                                  action="branch")))
    if callback_query["language"] == "uzb":
        if son == 1:
            await bot.send_message(message.from_user.id,
                                   "Filialingizga qaysi maxsulotdan qo'shmoqchisiz🤨\n\n🧐Yoki yangi qo'shiladigan maxsulot nomini kiriting.",
                                   reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,
                                   "Filialingizga yangi qo'shiladigan maxsulotni nomini kiriting")

    elif callback_query["language"] == "eng":
        if son == 1:
            await bot.send_message(message.from_user.id,
                                   "Which product do you want to add to your branch🤨\n\n🧐Or type the name of the new product to be added in this view: Name,price",
                                   reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,
                                   "Write a new product to be added to your branch in the following form: Name,price")

    elif callback_query["language"] == "rus":
        if son == 1:
            await bot.send_message(message.from_user.id,
                                   "Какой продукт вы хотите добавить в свою ветку🤨\n\n🧐Или введите имя нового продукта, который будет добавлен в этом представлении: Название,цена",
                                   reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,
                                   "Напишите новый продукт, который будет добавлен в вашу ветку в следующей форме: Название,цена")
    conn.execute(f"update ADMIN_ set spare = (?), tur = '{callback_query['stage']}' where id = (?);",
                 (admin[0], message.from_user.id))
    conn.execute("update ADMIN set settings = 'add_spare name' where id = (?);", (message.from_user.id,))


async def admin_button(message: types.Message, conn: sqlite3.Connection, callback_query: dict):
    """

    :param message:
    :param conn:
    :param callback_query:
    """
    conn.execute("update ADMIN_ set spare = (?) where id = (?)", (callback_query["name"], message.from_user.id))
    conn.execute("update ADMIN set settings = 'many' where id = (?);", (message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "Maxsulot narxini kiriting!")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "Введите цену товара!")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Enter the product price!")


async def admin_many(message: types.Message, conn: sqlite3.Connection, language: str):
    """

    :param message:
    :param conn:
    :param language:
    """
    car = conn.execute("select spare from ADMIN_ where id = (?);", (message.from_user.id,)).fetchall()[0]
    admin = conn.execute("select branch from ADMIN where id = (?);", (message.from_user.id,)).fetchall()[0]
    snow = conn.execute("select branches, tur, spare_name from SPARE where number = (?);", (car[0],)).fetchall()[0]
    son = None
    for i in snow[0].split("."):
        if i.split(",")[0] == admin[0]:
            son = 1
            break
    if son is None:
        conn.execute(
            f"update SPARE set branches = '{snow[0] + '.' + str(admin[0]) + ',' + message.text}' where number = (?);",
            (admin[0],))
        conn.execute(f"insert into BRANCH_SPARE(id,turi,spare_name,price,branch) values (?,?,?,?,?);",
                     (car[0], snow[1], snow[2], message.text, admin[0]))
        if language == "uzb":
            await bot.send_message(message.from_user.id, f"Qo'shildi✅")
        elif language == "eng":
            await bot.send_message(message.from_user.id, f"Added✅")
        elif language == "rus":
            await bot.send_message(message.from_user.id, f"Добавлено✅")
    elif son is not None:
        if admin[3] == "uzb":
            await bot.send_message(message.from_user.id, "Siz oldin ham buni qo'shgansiz.")
        elif admin[3] == "rus":
            await bot.send_message(message.from_user.id, "Вы добавили это раньше.")
        elif admin[3] == "eng":
            await bot.send_message(message.from_user.id, "You’ve added this before.")
    conn.execute("update ADMIN set settings = '0' where id = (?);", (message.from_user.id,))
