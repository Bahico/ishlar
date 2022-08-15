import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..menu.menu import client_menu
from ..settings.number import get_message_number

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_message(message: types.Message, conn: sqlite3.Connection,
                         vote_cb: aiogram.utils.callback_data.CallbackData):
    client = conn.execute("select settings, language from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    if client[0][1] == "uzb":
        client = client[0]
        if client[0] == "spare_number":
            try:
                int(message.text)
                await get_message_number(message, conn, vote_cb, client)
            except:
                await bot.send_message(message.from_user.id, "Iltimos faqat son kiriting!")
                conn.execute("update CLIENT set settings = '0' where id = (?);", (message.from_user.id,))

        elif client[0] == "my_number":
            try:
                son = 0
                phone_number = message.text
                for i in phone_number:
                    if son == 0:
                        son = 1
                    else:
                        int(i)
                conn.execute("update CLIENT set settings = 'my_location', phone_number = (?)  where id = (?);",
                             (phone_number[1:], message.from_user.id))
                markup = ReplyKeyboardMarkup()
                markup.add(KeyboardButton(text="🗺 Turgan joyim", request_location=True))
                await bot.send_message(message.from_user.id, "Turgan joyingizni kiriting.", reply_markup=markup)
            except:
                await bot.send_message(message.from_user.id, "Iltimos to'gri kiriting\n\n+************")

        elif client[0] == "phone_number_add":
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            try:
                son = 0
                phone_number = message.text
                for i in phone_number:
                    if son == 0:
                        son = 1
                    else:
                        int(i)
                conn.execute("update CLIENT set settings = '0', phone_number = (?)  where id = (?);",
                             (phone_number[1:], message.from_user.id))
                await client_menu(message, vote_cb, client[1])
            except:
                await bot.send_message(message.from_user.id, "Iltimos to'gri kiriting\n\n+************")

    #   -----RUS MESSAGE------
    elif client[0][1] == "rus":
        client = client[0]
        if client[0] == "spare_number":
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            try:
                int(message.text)
                await get_message_number(message, conn, vote_cb, client)
            except:
                await bot.send_message(message.from_user.id, "Пожалуйста, просто введите число!")
                conn.execute("update CLIENT set settings = '0' where id = (?);", (message.from_user.id,))

        elif client[0] == "my_number":
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            try:
                son = 0
                phone_number = message.text
                for i in phone_number:
                    if son == 0:
                        son = 1
                    else:
                        int(i)
                conn.execute("update CLIENT set settings = 'my_location', phone_number = (?)  where id = (?);",
                             (phone_number[1:], message.from_user.id))
                markup = ReplyKeyboardMarkup()
                markup.add(KeyboardButton(text="🗺 Место нахождения", request_location=True))
                await bot.send_message(message.from_user.id, "Введите свое местоположение.", reply_markup=markup)
            except:
                await bot.send_message(message.from_user.id, "Пожалуйста, введите правильно\n\n+************")

        elif client[0] == "phone_number_add":
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            try:
                son = 0
                phone_number = message.text
                for i in phone_number:
                    if son == 0:
                        son = 1
                    else:
                        int(i)
                conn.execute("update CLIENT set settings = '0', phone_number = (?)  where id = (?);",
                             (phone_number[1:], message.from_user.id))
                await client_menu(message, vote_cb, client[1])
            except:
                await bot.send_message(message.from_user.id, "Пожалуйста, введите правильно\n\n+************")

    #  -----ENG MESSAGE------
    elif client[0][1] == "eng":
        client = client[0]
        if client[0] == "spare_number":
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            try:
                int(message.text)
                await get_message_number(message, conn, vote_cb, client)
            except:
                await bot.send_message(message.from_user.id, "Please just enter a number!")
                conn.execute("update CLIENT set settings = '0' where id = (?);", (message.from_user.id,))

        elif client[0] == "my_number":
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            try:
                son = 0
                phone_number = message.text
                for i in phone_number:
                    if son == 0:
                        son = 1
                    else:
                        int(i)
                conn.execute("update CLIENT set settings = 'my_location', phone_number = (?)  where id = (?);",
                             (phone_number[1:], message.from_user.id))
                markup = ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(KeyboardButton(text="🗺 Location", request_location=True))
                await bot.send_message(message.from_user.id, "Enter your location.", reply_markup=markup)
            except:
                await bot.send_message(message.from_user.id, "Please enter correctly\n\n+************")

        elif client[0] == "phone_number_add":
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            try:
                son = 0
                phone_number = message.text
                for i in phone_number:
                    if son == 0:
                        son = 1
                    else:
                        int(i)
                conn.execute("update CLIENT set settings = '0', phone_number = (?)  where id = (?);",
                             (phone_number[1:], message.from_user.id))
                await client_menu(message, vote_cb, client[1])
            except:
                await bot.send_message(message.from_user.id, "Please enter correctly\n\n+************")
