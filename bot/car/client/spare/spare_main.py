from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from client.car_arr.car_name import client_car_name
from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_spare_number(message: types.Message, conn, vote_cb, callback_query):
    """

    :param message:
    :param conn:
    :param vote_cb:
    :param callback_query:
    :return:
    """

    car = conn.execute(f"select spare_name, number from SPARE where id = (?) and tur = '{callback_query['stage']}';",(callback_query["name"],)).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    son = 0
    for i in car:
        son = 1
        markup.add(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(stage=callback_query["stage"], id="spare",name=i[1],number="",language=callback_query["language"],action="client")))

    if callback_query["language"] == "uzb":
        if son == 1:
            await bot.send_message(message.from_user.id, "Kerakli extiyot qismni tanlang.", reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id, "Hali bu moshinaga maxsulot qo'shilmagan.")
            await client_car_name(message,conn,vote_cb,callback_query["language"])
    elif callback_query["language"] == "rus":
        if son == 1:
            await bot.send_message(message.from_user.id, "Выберите нужную часть.", reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"На эту машину еще не было добавлено ни одного продукта.")
            await client_car_name(message,conn,vote_cb,callback_query["language"])
    elif callback_query["language"] == "eng":
        if son == 1:
            await bot.send_message(message.from_user.id, "Select the desired part.", reply_markup=markup)
        else:
            await bot.send_message(message.from_user.id,"No product has been added to this machine yet.")
            await client_car_name(message,conn,vote_cb,callback_query["language"])
