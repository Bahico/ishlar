from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from client.menu.menu import client_menu
from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_contact(message: types.Message, conn, vote_cb):
    """
    Contactini saqlaydi
    :param vote_cb:
    :param message:
    :param conn:
    :return: location so'raydi
    """
    client = conn.execute("select settings, language from CLIENT where id = (?);", (message.from_user.id,)).fetchall()[0]
    if client and client[0] == "my_number":
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        conn.execute(
            f"update CLIENT set settings = 'my_location', phone_number = {str(message.contact.phone_number)[1:]} where id = {message.from_user.id};")
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(text="🗺 Turgan joyim", request_location=True))
        await bot.send_message(message.from_user.id, "Turgan joyingizni kiriting.", reply_markup=markup)
    elif client and client[0] == "phone_number_add":
        conn.execute(
            f"update CLIENT set settings = '0', phone_number = {str(message.contact.phone_number)[1:]} where id = {message.from_user.id};")
        await client_menu(message, conn, vote_cb, client[1])
