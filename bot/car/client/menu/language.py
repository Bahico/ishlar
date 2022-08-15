from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from client.menu.menu import client_menu
from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_edit_language(message: types.Message, vote_cb, callback_query):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    if callback_query["language"] == "uzb":
        markup.row(
            InlineKeyboardButton(text="🇷🇺 Русский",
                                 callback_data=vote_cb.new(stage="language_add", id="main_menu",name="None",number="None", language="rus",action="client")),
            InlineKeyboardButton(text="🇬🇧 English",
                                 callback_data=vote_cb.new(stage="language_add", id="main_menu",name="None", number="None",language="eng",action="client")),
            InlineKeyboardButton(text="⬅️ Ortga",
                                 callback_data=vote_cb.new(stage="back", id="main_menu",name="None",number="None", language="back",action="client")),
        )
        await bot.send_message(message.from_user.id, "Qaysi tilga o'zgartirish kerak?", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(
            InlineKeyboardButton(text="🇺🇿 O'zbek",
                                 callback_data=vote_cb.new(stage="language_add", id="main_menu",name="None",number="None", language="uzb",action="client")),
            InlineKeyboardButton(text="🇬🇧 English",
                                 callback_data=vote_cb.new(stage="language_add", id="main_menu",name="None", number="None",language="eng",action="client")),
            InlineKeyboardButton(text="⬅️ Ortga",
                                 callback_data=vote_cb.new(stage="back", id="main_menu",name="None",number="None", language="rus",action="client")),
        )
        await bot.send_message(message.from_user.id, "На какой язык вы меняете язык?", reply_markup=markup)

    elif callback_query["language"] == "eng":
        markup.row(
            InlineKeyboardButton(text="🇺🇿 O'zbek",
                                 callback_data=vote_cb.new(stage="language_add", id="main_menu",name="None",number="None", language="uzb",action="client")),
            InlineKeyboardButton(text="🇷🇺 Русский",
                                 callback_data=vote_cb.new(stage="language_add", id="main_menu",name="None", number="None",language="rus",action="client")),
            InlineKeyboardButton(text="⬅️ Ortga",
                                 callback_data=vote_cb.new(stage="back", id="main_menu", name="None", number="None", language="eng", action="client")),
        )
        await bot.send_message(message.from_user.id, "На какой язык вы меняете язык?", reply_markup=markup)


async def client_language_edit(message: types.Message, conn, vote_cb, callback_query):
    conn.execute(f"update CLIENT set language = {callback_query['language']} where id = (?);", (message.from_user.id,))
    await client_menu(message, conn, vote_cb, callback_query["language"])
