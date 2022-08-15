from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

# "id", "language", "name", "number", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_edit_phone_number(message:types.Message,conn,callback_query):
    conn.execute("update CLIENT set settings = 'phone_number_add' where id = (?);",(message.from_user.id,))
    markup = ReplyKeyboardMarkup()
    if callback_query["language"] == "uzb":
        markup.add(KeyboardButton("📱Telefon raqamim",request_contact=True))
        await bot.send_message(message.from_user.id,"Raqamingizni o'zgartirish uchun shu ko'rinishida kiriting: +**********\n\nYoki \"📱Telefon raqamim\" Tugmasini bosing",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.add(KeyboardButton("📱Мой номер телефона",request_contact=True))
        await bot.send_message(message.from_user.id,"Чтобы изменить свой номер, войдите в это представление: +**********\n\nИли \"📱Мой номер телефона\" нажми на кнопку",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.add(KeyboardButton("📱My phone number",request_contact=True))
        await bot.send_message(message.from_user.id,"To change your number, enter this view: +**********\n\nOr \"📱My phone number\" press the button",reply_markup=markup)
