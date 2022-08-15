import sqlite3
from datetime import datetime

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

from client.delivery.branch import get_branch_menu
from client.start import start
from client.message.main_message import get_message_client, get_start
from client.main_menu.main_menu import get_menu_client
from client.callback.callback import get_callback_client
from client.client_location.location import get_client_location
from admin.start.start import get_start_admin
from admin.message.main_message import get_message_admin
from admin.menu.main_menu import get_admin_menu
from admin.callback.callback import get_admin_callback
from admin.update_photo.update_photo import get_photo

from config import TOKEN, code

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_contact(message: types.Message, conn):
    phone_number = str(message.contact.phone_number)
    person = conn.execute("select * from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    admin = conn.execute("select bosqich from ADMIN where id = (?);", (message.from_user.id,)).fetchall()
    if person and admin:
        await bot.send_message(message.from_user.id, "Iltimos chatga /logout deb yozib keyn foydalaning.")
    elif person and not admin:
        conn.execute("update CLIENT set phone_number = (?) where id = (?);", (phone_number[3:], message.from_user.id))
        person = conn.execute("select language from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
        await get_branch_menu(message, conn, person[0][0])
    elif admin:
        if admin[0][0] == 2:
            conn.execute("update ADMIN set name = (?), phone_number = (?), bosqich = 3 where id = (?);",
                         (message.contact.full_name, phone_number[3:], message.from_user.id))
            await bot.send_message(message.from_user.id, "Password:", reply_markup=ReplyKeyboardRemove())
