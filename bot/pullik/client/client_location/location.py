import sqlite3
from datetime import datetime

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_client_location(message: types.Message, conn):
    branch = conn.execute("select latitude, longitude, name, id from BRANCH;").fetchall()
    person = conn.execute("select language from CLIENT where id = (?);",(message.from_user.id,)).fetchall()
    person = person[0]
    son = 0
    branch_name = None
    for i in branch:
        son = 0
        if i[0] - 0.01 <= message.location.latitude and i[1] - 0.01 <= message.location.longitude:
            if i[0] + 0.01 >= message.location.latitude and i[1] + 0.01 >= message.location.longitude:
                conn.execute("update CLIENT set delivery = (?) where id = (?);", ("delivery", message.from_user.id))
                son += 1
                branch_name = i
                # await bot_.send_location(message.from_user.id, message.location.latitude, message.location.longitude)
    if person[0] == "uzb":
        if son == 1 or son != 0:
            await bot.send_message(message.from_user.id, f"Siz {branch_name[2]} filialdan foydalanyapsiz.")
            conn.execute("update CLIENT set branch = (?) where id = (?);", (branch_name[3], message.from_user.id))
            conn.execute("update CLIENT set delivery = (?), bosqich = 13 where id = (?);", ("delivery", message.from_user.id))
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton("📱 Mening Telefon raqamim",request_contact=True))
            markup.add(KeyboardButton("⬅️ Ortga"))
            await bot.send_message(message.from_user.id,"Raqamingizni +998********* shu ko'rinishida kiriting yoki yuboring.",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,
                                   "Filiallar zo'nasidan tashqaridasiz.\n\nLekin olib ketishingiz mumkin.")
    elif person[0] == "rus":
        if son == 1 or son != 0:
            await bot.send_message(message.from_user.id, f"Siz {branch_name[2]} filialdan foydalanyapsiz.")
            conn.execute("update CLIENT set branch = (?) where id = (?);", (branch_name[3], message.from_user.id))
            conn.execute("update CLIENT set delivery = (?), bosqich = 13 where id = (?);", ("delivery", message.from_user.id))
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton("📱 Mening Telefon raqamim",request_contact=True))
            markup.add(KeyboardButton("⬅️ Ortga"))
            await bot.send_message(message.from_user.id,"Raqamingizni +998********* shu ko'rinishida kiriting yoki yuboring.",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,
                                   "Filiallar zo'nasidan tashqaridasiz.\n\nLekin olib ketishingiz mumkin.")
    elif person[0] == "eng":
        if son == 1 or son != 0:
            await bot.send_message(message.from_user.id, f"Siz {branch_name[2]} filialdan foydalanyapsiz.")
            conn.execute("update CLIENT set branch = (?) where id = (?);", (branch_name[3], message.from_user.id))
            conn.execute("update CLIENT set delivery = (?), bosqich = 13 where id = (?);", ("delivery", message.from_user.id))
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton("📱 Mening Telefon raqamim",request_contact=True))
            markup.add(KeyboardButton("⬅️ Ortga"))
            await bot.send_message(message.from_user.id,"Raqamingizni +998********* shu ko'rinishida kiriting yoki yuboring.",reply_markup=markup)
        elif son == 0:
            await bot.send_message(message.from_user.id,
                                   "Filiallar zo'nasidan tashqaridasiz.\n\nLekin olib ketishingiz mumkin.")
