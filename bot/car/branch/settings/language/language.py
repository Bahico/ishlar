from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_adit_language(message: types.Message, conn, vote_cb, callback_query):
    if callback_query["language"] == "uzb":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="🇷🇺 Русский",
                                 callback_data=vote_cb.new(stage="rus", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="rus", action="branch")),
            InlineKeyboardButton(text="🇬🇧 English",
                                 callback_data=vote_cb.new(stage="eng", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="eng", action="branch"))
        )
        await bot.send_message(message.from_user.id, "Hozir sizning tilingiz 🇺🇿O'zbek tilida", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="🇺🇿 O'zbek",
                                 callback_data=vote_cb.new(stage="uzb", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="uzb", action="branch")),
            InlineKeyboardButton(text="🇬🇧 English",
                                 callback_data=vote_cb.new(stage="eng", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="eng", action="branch"))
        )
        await bot.send_message(message.from_user.id, "Сейчас ваш язык будет 🇷🇺Русский ", reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="🇺🇿 O'zbek",
                                 callback_data=vote_cb.new(stage="uzb", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="uzb", action="branch")),
            InlineKeyboardButton(text="🇷🇺 Русский",
                                 callback_data=vote_cb.new(stage="rus", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="rus", action="branch"))
        )
        await bot.send_message(message.from_user.id, "Currently, your language is English", reply_markup=markup)


async def admin_language_edit(message: types.Message, conn, vote_cb, callback_query):
    conn.execute(f"update ADMIN set language = '{callback_query['language']}' where id = (?);", (message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "🇺🇿 O'zbek tiliga o'zgartirildi.")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id,"Ваш язык был изменен на 🇷🇺 Русский.")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id,"Your language has been changed to 🇬🇧 English.")