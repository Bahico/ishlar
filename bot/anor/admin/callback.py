import sqlite3

import aiogram
from aiogram import Bot, Dispatcher, types

from admin.menu import admin_menu
from admin.payment import admin_payment_category, admin_payment_fan, admin_payment_user, admin_payment_price
from admin.user.add_user import admin_user_category, admin_user_lessen, admin_user_name
from admin.category import admin_category
from admin.edit_code import admin_code_edit_call
from admin.lessen import admin_lessen_category, admin_lessen_fan
from admin.user.excel_file import admin_user_excel
from admin.user.main import admin_user
from admin.user.open_user import admin_user_pagination, admin_user_information, admin_user_delete
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_callback(message: types.CallbackQuery, vote_cb: aiogram.utils.callback_data.CallbackData,
                         main_conn: sqlite3.Connection, callback_query: dict):
    if callback_query["stage"] == "lessen":
        if callback_query["stage1"] == "add":
            await admin_lessen_category(message, vote_cb, main_conn)
        elif callback_query["stage1"] == "category":
            await admin_lessen_fan(message, vote_cb, main_conn, callback_query)

    elif callback_query["stage"] == "category":
        if callback_query["stage1"] == "add":
            await admin_category(message, main_conn)

    elif callback_query["stage"] == "code":
        if callback_query["stage1"] == "edit":
            await admin_code_edit_call(message, main_conn)

    elif callback_query["stage"] == "user":
        if callback_query["stage1"] == "user":
            await admin_user(message, vote_cb)
        elif callback_query["stage1"] == "excel":
            await admin_user_excel(message, main_conn, vote_cb)
        elif callback_query["stage1"] == "pagination":
            await admin_user_pagination(message, main_conn, vote_cb, callback_query)
        elif callback_query["stage1"] == "information":
            await admin_user_information(message, main_conn, vote_cb, callback_query)
        elif callback_query["stage1"] == "delete":
            await admin_user_delete(main_conn, callback_query["tur"])
            await bot.send_message(message.from_user.id, "O'chirildi")
            await admin_menu(message, vote_cb)

    elif callback_query["stage"] == "add user":
        if callback_query["stage1"] == "add":
            await admin_user_category(message, main_conn, vote_cb)
        elif callback_query["stage1"] == "category":
            await admin_user_lessen(message, main_conn, vote_cb, callback_query)
        elif callback_query["stage1"] == "fan":
            await admin_user_name(message, main_conn, callback_query)

    elif callback_query["stage"] == "payment":
        if callback_query["stage1"] == "payment":
            await admin_payment_category(message, main_conn, vote_cb)
        elif callback_query["stage1"] == "category":
            await admin_payment_fan(message, main_conn, vote_cb, callback_query)
        elif callback_query["stage1"] == "fan":
            await admin_payment_user(message, main_conn, vote_cb, callback_query)
        elif callback_query["stage1"] == "student":
            await admin_payment_price(message, main_conn, callback_query)
