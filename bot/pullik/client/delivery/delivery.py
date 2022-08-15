from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_delivery(message: types.Message, conn,  language):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    conn.execute("update CLIENT set bosqich = (?) where id = (?);",(2,message.from_user.id))
    if language == "uzb":
        markup.add(KeyboardButton(text="🚙 Yetkazib berish",request_location=True))
        markup.add(KeyboardButton(text="🏃 Olib ketish"))
        markup.add(KeyboardButton(text="⬅️ Ortga"))
        await bot.send_message(message.from_user.id, "Buyurtmani o'zingiz olib ketasizmi yoki yetkazib beramizmi?",reply_markup=markup)
    elif language == "rus":
        markup.add(KeyboardButton(text="🚙 Доставка"))
        markup.add(KeyboardButton(text="🚙 Забрать"))
        markup.add(KeyboardButton(text="⬅️ Назад"))
        await bot.send_message(message.from_user.id, "Вы сами примете заказ или мы доставим?",reply_markup=markup)
    elif language == "eng":
        markup.add(KeyboardButton(text="🚙 Delivery"))
        markup.add(KeyboardButton(text="🏃 Take away"))
        markup.add(KeyboardButton(text="⬅️ Back"))
        await bot.send_message(message.from_user.id, "Will you take the order yourself or will we deliver?",reply_markup=markup)
