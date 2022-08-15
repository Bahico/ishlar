from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_menu(message: types.Message, conn, vote_cb, language):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    if language == "uzb":
        markup.row(
            InlineKeyboardButton(text="📱 Telefon raqamim",
                                 callback_data=vote_cb.new(stage="phone_number", id="main_menu",name="None",number="None", language=language,action="client")),
            InlineKeyboardButton(text="🇺🇿 Tilni o'zgartirish",
                                 callback_data=vote_cb.new(stage="language_edit", id="main_menu",name="None",number="None", language=language,action="client")))
        markup.add(
            InlineKeyboardButton(text="📖 Haridlar tarixi",
                                 callback_data=vote_cb.new(stage="history", id="main_menu",name="None",number="None", language=language,action="client"))
        )
        await bot.send_message(message.from_user.id, "Tanlang👇🏻👇🏻", reply_markup=markup)
    elif language == "rus":
        markup.row_width = 2
        markup.row(
            InlineKeyboardButton(text="📱 Мой номер телефона",
                                 callback_data=vote_cb.new(stage="phone_number", id="main_menu",name="None",number="None", language=language,action="client")),
            InlineKeyboardButton(text="🇷🇺 Изменить язык",
                                 callback_data=vote_cb.new(stage="language_edit", id="main_menu",name="None",number="None", language=language,action="client")))
        markup.add(
            InlineKeyboardButton(text="📖 История покупки",
                                 callback_data=vote_cb.new(stage="history", id="main_menu",name="None",number="None", language=language,action="client"))
        )
        await bot.send_message(message.from_user.id, "Выбирать🏻👇🏻", reply_markup=markup)
    elif language == "eng":
        markup.row_width = 2
        markup.row(
            InlineKeyboardButton(text="📱 My phone number",
                                 callback_data=vote_cb.new(stage="phone_number", id="main_menu",name="None",number="None", language=language,action="client")),
            InlineKeyboardButton(text="🇬🇧 Change the language",
                                 callback_data=vote_cb.new(stage="language_edit", id="main_menu",name="None",number="None", language=language,action="client")))
        markup.add(
            InlineKeyboardButton(text="📖 Purchase history",
                                 callback_data=vote_cb.new(stage="history", id="main_menu",name="None",number="None", language=language,action="client"))
        )
        await bot.send_message(message.from_user.id, "Select👇🏻👇🏻", reply_markup=markup)
