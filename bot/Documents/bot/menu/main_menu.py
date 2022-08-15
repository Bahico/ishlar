import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_main_menu(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData, language: str, conn: sqlite3.Connection):
    conn.execute(f"update I_ set language = '{language}' where id = (?);", (message.from_user.id,))
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    print(True)
    if language == "uzb":
        markup.row(
            InlineKeyboardButton(text="🏘Filiallar",
                                 callback_data=vote_cb.new(stage="branches", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="👨Odamlar soni",
                                 callback_data=vote_cb.new(stage="people", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
        )
        markup.row(
            InlineKeyboardButton(text="🤖Bot kodini o'zgartirish",
                                 callback_data=vote_cb.new(stage="code_edit", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="❌Maxsulot o'chirish",
                                 callback_data=vote_cb.new(stage="spare_del", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
        )
        markup.add(
            InlineKeyboardButton(text="Marka qo'shish",
                                 callback_data=vote_cb.new(stage="corporation add", id="main_menu", name="None",
                                                           number="10", language=language, action="bot"))
        )
        await bot.send_message(message.from_user.id, "Bot sozlamalari👇🏻👇🏻", reply_markup=markup)
    #   ------RUS MESSAGE----
    elif language == "rus":
        markup.row(
            InlineKeyboardButton(text="🏘Ветви",
                                 callback_data=vote_cb.new(stage="branches", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="👨Число людей",
                                 callback_data=vote_cb.new(stage="people", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
        )
        markup.row(
            InlineKeyboardButton(text="🤖Изменить код бота",
                                 callback_data=vote_cb.new(stage="code_edit", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="❌Удаление продукта",
                                 callback_data=vote_cb.new(stage="spare_del", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
        )
        markup.add(
            InlineKeyboardButton(text="Marka qo'shish",
                                 callback_data=vote_cb.new(stage="corporation add", id="main_menu", name="None",
                                                           number="10", language=language, action="bot"))
        )
        await bot.send_message(message.from_user.id, "Настройки бота👇🏻👇🏻", reply_markup=markup)
    #   -----ENG MESSAGE----
    elif language == "eng":
        markup.row(
            InlineKeyboardButton(text="🏘Branches",
                                 callback_data=vote_cb.new(stage="branches", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="👨Number of people",
                                 callback_data=vote_cb.new(stage="people", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="🤖Change the bot code",
                                 callback_data=vote_cb.new(stage="code_edit", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="❌Product removal",
                                 callback_data=vote_cb.new(stage="spare_del", id="main_menu", name="None", number="10",
                                                           language=language, action="bot")),
            InlineKeyboardButton(text="Marka qo'shish",
                                 callback_data=vote_cb.new(stage="corporation add", id="main_menu", name="None",
                                                           number="10", language=language, action="bot"))
        )
        await bot.send_message(message.from_user.id, "Bot settings👇🏻👇🏻", reply_markup=markup)
