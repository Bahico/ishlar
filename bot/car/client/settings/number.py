from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from client.car_arr.car_name import client_car_name
from config import TOKEN

# some code

# "id", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_message_number(message: types.Message, conn, vote_cb, client):
    """
    Client ning telefon nomerini yozma ravishda oladi
    :param client: client malumotlari
    :param message:
    :param conn:
    :param vote_cb:
    :return: Yana biror narsa olishi uchun imkon beradi
    """
    spare = conn.execute("select basket, spare from CLIENT_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    if client[0] is None:
        conn.execute(f"update CLIENT_ set basket = '{message.text + ',' + spare[1]}' where id = (?);",(message.from_user.id,))
    else:
        conn.execute(f"update CLIENT_ set basket = '{spare[0] + '.' + message.text + ','+ spare[1]}' where id = (?);",(message.from_user.id,))

    if client[1] == "uzb":
        await bot.send_message(message.from_user.id, "Yana biror narsa kerakmi?😊")
    elif client[1] == "rus":
        await bot.send_message(message.from_user.id, "Хотели бы вы что-нибудь еще? 😊")
    elif client[1] == "eng":
        await bot.send_message(message.from_user.id, "Would you like anything else? 😊")
    await client_car_name(message, conn, vote_cb, client[1])
