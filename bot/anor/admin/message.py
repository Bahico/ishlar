import sqlite3

import aiogram
from aiogram import Bot, Dispatcher, types

from admin.payment import admin_payment_date, admin_payment_finish
from admin.user.add_user import admin_user_phone, admin_user_add
from admin.category import admin_add_category
from admin.edit_code import admin_code_edit_mes
from admin.lessen import admin_lessen_description, admin_lesson_finish
from admin.start import admin_password
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_message(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData,
                        main_conn: sqlite3.Connection):
    text = main_conn.execute("select text from all_user where id = (?);", (message.from_user.id,)).fetchall()[0][0]
    if text == "add category":
        await admin_add_category(message, vote_cb, main_conn)
    elif text == "add fan name":
        await admin_lessen_description(message, main_conn)
    elif text == "add fan price":
        await admin_lesson_finish(message, vote_cb, main_conn)
    elif text == "password":
        await admin_password(message, main_conn, vote_cb)
    elif text == "edit code":
        await admin_code_edit_mes(message, main_conn, vote_cb)
    elif text == "add user name":
        await admin_user_phone(message, main_conn)
    elif text == "add user phone number":
        try:
            int(message.text)
            await admin_user_add(message, main_conn, vote_cb)
        except:
            await bot.send_message(message.from_user.id, "Iltimos faqat son kiriting")
    elif text == "payment money":
        try:
            int(message.text)
            await admin_payment_date(message, main_conn)
        except:
            await message.answer("Iltimos faqat son kiriting")
    elif text == "payment date":
        await admin_payment_finish(message, main_conn, vote_cb)
