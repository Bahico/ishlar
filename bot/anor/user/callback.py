import sqlite3

import aiogram
from aiogram import Bot, Dispatcher, types

from config import TOKEN
from user.course.course import user_course, user_fan
from user.start.payments import user_payments_lessen
from user.start.start import user_start

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def user_callback(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                        main_conn: sqlite3.Connection, callback_query: dict):
    if callback_query["stage"] == "start":
        if callback_query["tur"] == "payments":
            pass
        elif callback_query["tur"] == "courses":
            await user_course(message, vote_cb, main_conn)
        elif callback_query["tur"] == "fan":
            await user_fan(message, vote_cb, main_conn, callback_query)
        elif callback_query["tur"] == "about":
            pass
    elif callback_query["stage"] == "payments":
        if callback_query["stage1"] == "course":
            await user_payments_lessen(message, vote_cb, main_conn, callback_query)
        elif callback_query["stage1"] == "fan":
            pass
    elif callback_query["stage"] == "back":
        await user_start(message, vote_cb, main_conn)
