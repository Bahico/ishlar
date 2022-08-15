from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from ..food import fast_food, waffle, drinks, coffee

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_callback(message: types.Message, conn, person, language):
    if language == "uzb":
        if message.text == "🧇 Vaflilar":
            await waffle.get_waffle(message, conn, "uzb", person[2])
        elif message.text == "🧃 Salqin ichimliklar":
            await drinks.get_drinks(message, conn, "uzb", person[2])
        elif message.text == "☕️ Coffee":
            await coffee.get_coffee(message, conn, "uzb", person[2])
        elif message.text == "🍔️ Fast Food":
            await fast_food.get_fast_food(message, conn, "uzb", person[2])
    elif language == "rus":
        if message.text == "🧇 Вафли":
            await waffle.get_waffle(message, conn, "rus", person[2])
        elif message.text == "🧃 Прохладительные напитки":
            await drinks.get_drinks(message, conn, "rus", person[2])
        elif message.text == "☕️ Coffee":
            await coffee.get_coffee(message, conn, "rus", person[2])
        elif message.text == "🍔️️ Быстрое питание":
            await fast_food.get_fast_food(message, conn, "rus", person[2])
    elif language == "eng":
        if message.text == "🧇 Waffles":
            await waffle.get_waffle(message, conn, "eng", person[2])
        elif message.text == "🧃 Cool drinks":
            await drinks.get_drinks(message, conn, "eng", person[2])
        elif message.text == "☕️ Coffee":
            await coffee.get_coffee(message, conn, "eng", person[2])
        elif message.text == "🍔️️ Fast Food":
            await fast_food.get_fast_food(message, conn, "eng", person[2])

