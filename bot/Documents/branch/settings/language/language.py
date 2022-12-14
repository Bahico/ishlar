import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_adit_language(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                              callback_query: dict):
    if callback_query["language"] == "uzb":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน",
                                 callback_data=vote_cb.new(stage="rus", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="rus", action="branch")),
            InlineKeyboardButton(text="๐ฌ๐ง English",
                                 callback_data=vote_cb.new(stage="eng", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="eng", action="branch"))
        )
        await bot.send_message(message.from_user.id, "Hozir sizning tilingiz ๐บ๐ฟO'zbek tilida", reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="๐บ๐ฟ O'zbek",
                                 callback_data=vote_cb.new(stage="uzb", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="uzb", action="branch")),
            InlineKeyboardButton(text="๐ฌ๐ง English",
                                 callback_data=vote_cb.new(stage="eng", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="eng", action="branch"))
        )
        await bot.send_message(message.from_user.id, "ะกะตะนัะฐั ะฒะฐั ัะทัะบ ะฑัะดะตั ๐ท๐บะ ัััะบะธะน ", reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row(
            InlineKeyboardButton(text="๐บ๐ฟ O'zbek",
                                 callback_data=vote_cb.new(stage="uzb", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="uzb", action="branch")),
            InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน",
                                 callback_data=vote_cb.new(stage="rus", id="edit_language", name="None",
                                                           number=callback_query["number"],
                                                           language="rus", action="branch"))
        )
        await bot.send_message(message.from_user.id, "Currently, your language is English", reply_markup=markup)


async def admin_language_edit(message: types.Message, conn: sqlite3.Connection, callback_query: dict):
    conn.execute(f"update ADMIN set language = '{callback_query['language']}' where id = (?);", (message.from_user.id,))
    if callback_query["language"] == "uzb":
        await bot.send_message(message.from_user.id, "๐บ๐ฟ O'zbek tiliga o'zgartirildi.")
    elif callback_query["language"] == "rus":
        await bot.send_message(message.from_user.id, "ะะฐั ัะทัะบ ะฑัะป ะธะทะผะตะฝะตะฝ ะฝะฐ ๐ท๐บ ะ ัััะบะธะน.")
    elif callback_query["language"] == "eng":
        await bot.send_message(message.from_user.id, "Your language has been changed to ๐ฌ๐ง English.")
