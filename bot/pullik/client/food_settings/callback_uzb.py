from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..food import coffee, drinks, fast_food, waffle
from ..food_menu.food_menu import get_food_menu

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_callback(message: types.Message, conn, person, language):
    if language == "uzb":
        if message.text == "⬅️ Orqaga":
            tur = person[4].split(',')
            if tur[0] == "fast_food":
                await fast_food.get_fast_food(message, conn, "uzb", person[2])
            elif tur[0] == "coffee":
                await coffee.get_coffee(message, conn, "uzb", person[2])
            elif tur[0] == "drinks":
                await drinks.get_drinks(message, conn, "uzb", person[2])
            elif tur[0] == "waffle":
                await waffle.get_waffle(message, conn, "uzb", person[2])
        else:
            for i in range(1,10):
                if str(i) == message.text:
                    if person[4] is not None:
                        conn.execute("update CLIENT set basket = (?) where id = (?);",(person[4]+"."+person[3]+","+str(i),message.from_user.id))
                    else:
                        conn.execute("update CLIENT set basket = (?) where id = (?)",(person[3]+","+str(i),message.from_user.id))
                    await bot.send_message(message.from_user.id,"Ajoyib tanlov! 😍 Yana nimadir buyurtma beramizmi?")
                    await get_food_menu(message,conn,"uzb",person[2],0)

    elif language == "rus":
        if message.text == "⬅️ Назад":
            tur = person[4].split(',')
            if tur[0] == "fast_food":
                await fast_food.get_fast_food(message, conn, "rus", person[2])
            elif tur[0] == "coffee":
                await coffee.get_coffee(message, conn, "rus", person[2])
            elif tur[0] == "drinks":
                await drinks.get_drinks(message, conn, "rus", person[2])
            elif tur[0] == "waffle":
                await waffle.get_waffle(message, conn, "rus", person[2])
        else:
            for i in range(1,10):
                if str(i) == message.text:
                    if person[4] is not None:
                        conn.execute("update CLIENT set basket = (?) where id = (?);",(person[4]+"."+person[3]+","+str(i),message.from_user.id))
                    else:
                        conn.execute("update CLIENT set basket = (?)",(person[3]+","+str(i),message.from_user.id))
                    await bot.send_message(message.from_user.id,"Ajoyib tanlov! 😍 Yana nimadir buyurtma beramizmi?")
                    await get_food_menu(message,conn,"uzb",person[2],False)
    elif language == "eng":
        if message.text == "⬅️ Back":
            tur = person[4].split(',')
            if tur[0] == "fast_food":
                await fast_food.get_fast_food(message, conn, "eng", person[2])
            elif tur[0] == "coffee":
                await coffee.get_coffee(message, conn, "eng", person[2])
            elif tur[0] == "drinks":
                await drinks.get_drinks(message, conn, "eng", person[2])
            elif tur[0] == "waffle":
                await waffle.get_waffle(message, conn, "eng", person[2])
        else:
            for i in range(1,10):
                if str(i) == message.text:
                    if person[4] is not None:
                        conn.execute("update CLIENT set basket = (?) where id = (?);",(person[4]+"."+person[3]+","+str(i),message.from_user.id))
                    else:
                        conn.execute("update CLIENT set basket = (?)",(person[3]+","+str(i),message.from_user.id))
                    await bot.send_message(message.from_user.id,"Ajoyib tanlov! 😍 Yana nimadir buyurtma beramizmi?")
                    await get_food_menu(message,conn,"uzb",person[2],0)