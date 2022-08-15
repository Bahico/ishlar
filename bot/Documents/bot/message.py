import sqlite3

import aiogram.utils.callback_data
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.branch.branch_add import get_branch_add_login, get_branch_add_code, get_branch_add_branch
from bot.corporation import bot_corporation_insert
from bot.menu.main_menu import bot_main_menu
from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_message(message: types.Message, conn: sqlite3.Connection, vote_cb: aiogram.utils.callback_data.CallbackData, bot_: list):
    from config import code
    if bot_[0] == "start":
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        if message.text == code[0]:
            conn.execute("update I_ set test = 4, settings = '0' where id = (?);", (message.from_user.id,))
            markup = InlineKeyboardMarkup()
            markup.row(
                InlineKeyboardButton(text="🇷🇺 Pусский",
                                     callback_data=vote_cb.new(stage="language", id="start", name="None", number="10",
                                                               language="rus", action="bot")),
                InlineKeyboardButton(text="🇺🇿 O'zbekcha",
                                     callback_data=vote_cb.new(stage="language", id="start", name="None", number="10",
                                                               language="uzb", action="bot"))
            )
            markup.add(InlineKeyboardButton(text="🇬🇧 English",
                                            callback_data=vote_cb.new(stage="language", id="start", name="None",
                                                                      number="10", language="eng", action="bot")))
            await bot.send_message(message.from_user.id, "Select👇🏻👇🏻", reply_markup=markup)
        else:
            conn.execute("delete from I_ where id = (?);", (message.from_user.id,))
            await bot.send_message(message.from_user.id, "Error!")

    elif bot_[0] == "bot_code_edit":
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        conn.execute("update I_ set settings = NULL where id = (?);", (message.from_user.id,))
        from config import code
        code.clear()
        code.append(message.text)
        if bot_[1] == "uzb":
            await bot.send_message(message.from_user.id, "✅O'zgartirildi")
        elif bot_[1] == "rus":
            await bot.send_message(message.from_user.id, "✅Измененный")
        elif bot_[1] == "eng":
            await bot.send_message(message.from_user.id, "✅Changed")

        await bot_main_menu(message, vote_cb, bot_[1], conn)

    elif bot_[0] == "add_branch_name":
        await get_branch_add_login(message, conn, bot_)

    elif bot_[0] == "add_branch_login":
        await get_branch_add_code(message, conn, bot_)

    elif bot_[0] == "add_branch_code":
        await get_branch_add_branch(message, conn, vote_cb, bot_)

    elif bot_[0] == "add corporation":
        await bot_corporation_insert(message, conn, vote_cb, bot_)
