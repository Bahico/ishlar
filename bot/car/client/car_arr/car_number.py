from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from client.car_arr.car_pazitsiya import client_car_brand
from client.car_arr.print_car_spare import client_print_car

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_car_number(message: types.Message, conn, vote_cb, callback_query):
    client = conn.execute("select corporation from CLIENT_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    car = conn.execute(f"select number from CAR where corporation = {client[0]} and name = '{callback_query['name']}';").fetchall()
    conn.execute(f"update CLIENT_ set name = '{callback_query['name']}' where id = (?);",(message.from_user.id,))
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    car_set = set()
    for i in car:
        car_set.add(i[0])
    son = 0
    car_number = None
    sons = 0
    for i in car_set:
        if i != "bypass" and i is not None:
            son += 1
            car_number = i
            markup.insert(InlineKeyboardButton(text=f"{callback_query['name']} {str(i)}",callback_data=vote_cb.new(stage="car_number", id="start",name=i, number="", language=callback_query["language"],action="client")))
        elif i == "bypass":
            sons = 1
    callback_query["name"] = car_number
    if callback_query["language"] == "uzb":
        if son != 1 and son != 0:
            if sons == 1: markup.add(InlineKeyboardButton(text="Barcha rusumlarga ↪️",callback_data=vote_cb.new(stage="number", id="plus", name="bypass", number="", language=callback_query["language"], action="client")))
            await bot.send_message(message.from_user.id,f"\"{callback_query['name']}\" ni qaysi modelini ehtiyot qism kerak?",reply_markup=markup)
        elif son == 1:
            await client_car_brand(message, conn, vote_cb, callback_query)
    elif callback_query["language"] == "eng":
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id, f"Which model of \"{callback_query['name']}\" needs a spare?",reply_markup=markup)
        elif son == 1:
            await client_car_brand(message, conn, vote_cb, callback_query)
    elif callback_query["language"] == "rus":
        if son != 1 and son != 0:
            await bot.send_message(message.from_user.id, f"Для какой модели \"{callback_query['name']}\" нужна запчасть?",reply_markup=markup)
        elif son == 1:
            await client_car_brand(message, conn, vote_cb, callback_query)


async def client_number_bypass(message:types.Message,conn,vote_cb,callback_query):
    client = conn.execute("select corporation, name from car where id = (?);",(message.from_user.id,)).fetchall()[0]
    callback_query["name"] = conn.execute("select id from CAR where corporation = (?) and name = (?) and number ='bypass';",(client[0],client[1])).fetchall()[0][0]
    await client_print_car(message,conn, vote_cb, callback_query)