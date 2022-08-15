from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .print_car_spare import client_print_car

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_car_year(message:types.Message,conn,vote_cb,callback_query):
    client = conn.execute("select corporation, name, number from CLIENT_ where id = (?);",(message.from_user.id,)).fetchall()[0]
    conn.execute(f"update CLIENT_ set paditsiya = '{callback_query['name']}' where id = (?);",(message.from_user.id,))
    car = conn.execute(f"select year, id from CAR where corporation = {client[0]} and name = '{client[1]}' and number = '{client[2]}' and paditsiya = '{callback_query['name']}';").fetchall()
    son = 0
    sons = None
    soon = 0
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car:
        if i[0] == "bypass" and i is not None:
            son += 1
            sons = i[1]
            soon = 1
            markup.insert(InlineKeyboardButton(text=i[0],callback_data=vote_cb.new(stage="car_year", id="start",name=i[1], number="", language=callback_query["language"],action="client")))
    if son == 1:
        callback_query["name"] = sons
        await client_print_car(message, conn, vote_cb, callback_query)
    else:
        if callback_query["language"] == "uzb":
            if soon == 1: markup.add(InlineKeyboardButton(text="Barcha yillarga ↪️",callback_data=vote_cb.new(stage="year", id="plus", name="bypass", number="", language=callback_query["language"], action="client")))
            await bot.send_message(message.from_user.id,f"pass",reply_markup=markup)
        elif callback_query["language"] == "rus":
            await bot.send_message(message.from_user.id,f"pass")
        elif callback_query["language"] == "rus":
            await bot.send_message(message.from_user.id,"pass")


async def client_year_bypass(message:types.Message,conn,vote_cb,callback_query):
    client = conn.execute("select corporation, name, number, paditsiya from car where id = (?);",(message.from_user.id,)).fetchall()[0]
    callback_query["name"] = conn.execute("select id from CAR where corporation = (?) and name = (?) and number = (?) and paditsiya = (?) and year = 'bypass';",(client[0],client[1],client[2],client[3])).fetchall()[0][0]
    await client_print_car(message,conn, vote_cb, callback_query)