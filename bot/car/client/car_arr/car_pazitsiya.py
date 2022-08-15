from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .car_year import client_car_year

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"
from .print_car_spare import client_print_car

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_car_brand(message: types.Message, conn, vote_cb, callback_query):
    client = conn.execute("select corporation, name from CLIENT_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute(f"select paditsiya from CAR where corporation = {client[0]} and name = '{client[1]}' and number = '{callback_query['name']}';").fetchall()
    conn.execute(f"update CLIENT_ set number = '{callback_query['name']}' where id = (?);",(message.from_user.id,))
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    son = 0
    car_model = None
    sons = 0
    for i in car_set:
        if i != "bypass" and i is not None:
            son += 1
            car_model = i
            markup.add(InlineKeyboardButton(text=f"{i}",callback_data=vote_cb.new(stage="car_brand", id="start",name=i, number="", language=callback_query["language"],action="client")))
        elif i == "bypass":
            sons = 1
    callback_query["name"] = car_model
    if callback_query["language"] == "uzb":
        if son != 1 and son != 0:
            if sons == 1: markup.add(InlineKeyboardButton(text="Barcha pazitsiyalarga ↪️",callback_data=vote_cb.new(stage="paditsiya", id="plus", name="bypass", number="", language=callback_query["language"], action="client")))
            await bot.send_message(message.from_user.id,f"pass",reply_markup=markup)
        else:
            await client_car_year(message, conn, vote_cb, callback_query)
    elif callback_query["language"] == "rus":
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id,f"pass",reply_markup=markup)
        else:
            await client_car_year(message, conn, vote_cb, callback_query)
    elif callback_query["language"] == "eng":
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id, f"pass", reply_markup=markup)
        else:
            await client_car_year(message, conn, vote_cb, callback_query)


async def client_paditsiya_bypass(message:types.Message,conn,vote_cb,callback_query):
    client = conn.execute("select corporation, name, number from car where id = (?);",(message.from_user.id,)).fetchall()[0]
    callback_query["name"] = conn.execute("select id from CAR where corporation = (?) and name = (?) and number = (?) and paditsiya = 'bypass';",(client[0],client[1],client[2])).fetchall()[0][0]
    await client_print_car(message,conn, vote_cb, callback_query)