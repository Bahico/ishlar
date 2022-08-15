from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..food_menu import food_menu
from ..food_settings import food_number

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_callback(message: types.Message, conn, person,language):
    if language == "uzb" and message.text == "⬅️ Ortga":
        await food_menu.get_food_menu(message, conn, "uzb", person[3],True)
    elif language == "rus" and message.text == "⬅️ Назад":
        await food_menu.get_food_menu(message, conn, "rus", person[3],True)
    elif language == "eng" and message.text == "⬅️ Back":
        await food_menu.get_food_menu(message, conn, "eng", person[3],True)
    else:
        son = 0
        fast_food = conn.execute("select fast_food from BRANCH where id = (?);", (int(person[2]),)).fetchall()
        fast_food = fast_food[0][0].split('.')
        for i in fast_food:
            i = i.split(',')
            if i[0] == "True" and message.text == i[1]:
                son = 1
                conn.execute("update CLIENT set tur = (?) where id = (?);", ("fast_food,"+i[1],message.from_user.id))
                await food_number.get_number(message, conn, language, person[2], "fast_food", i[1])
        if son != 1:
            coffee = conn.execute("select coffee from BRANCH where id = (?);", (int(person[3]),)).fetchall()
            coffee = coffee[0][0].split('.')
            for i in coffee:
                i = i.split(',')
                if i[0] == "True" and message.text == i[1]:
                    son = 1
                    conn.execute("update CLIENT set tur = (?) where id = (?);", ("coffee,"+i[1],message.from_user.id))
                    await food_number.get_number(message, conn, language, person[3], "coffee", i[1])
        if son != 1:
            drinks = conn.execute("select drinks from BRANCH where id = (?);", (int(person[2]),)).fetchall()
            drinks = drinks[0][0].split('.')
            for i in drinks:
                i = i.split(',')
                if i[0] == "True" and message.text == i[1]:
                    son = 1
                    conn.execute("update CLIENT set tur = (?) where id = (?);", ("drinks,"+i[1],message.from_user.id))
                    await food_number.get_number(message, conn, language, person[3], "drinks", i[1])
        if son != 1:
            waffle = conn.execute("select waffle from BRANCH where id = (?);", (int(person[2]),)).fetchall()
            waffle = waffle[0][0].split('.')
            for i in waffle:
                i = i.split(',')
                if i[0] == "True" and message.text == i[1]:
                    son = 0
                    conn.execute("update CLIENT set tur = (?) where id = (?);", ("waffle,"+i[1],message.from_user.id))
                    await food_number.get_number(message, conn, language, person[3], "waffle", i[1])
