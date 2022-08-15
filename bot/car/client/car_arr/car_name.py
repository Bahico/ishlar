from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from client.car_arr.print_car_spare import client_print_car
from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_car_name(message: types.Message, conn, vote_cb, callback_query):
    """

    :param callback_query:
    :param message:
    :param conn:
    :param vote_cb:
    :return:
    """
    client = conn.execute("select basket from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()
    car = conn.execute("select name, id from car where corporation = (?);",(callback_query["name"],)).fetchall()
    car_set = set()
    for i in car:
        car_set.add(i[0])
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    son = 0
    for i in car_set:
        if i != "bypass" and i is not None: markup.insert(InlineKeyboardButton(text=i, callback_data=vote_cb.new(stage="car name", id="start", name=i, number="", language="uzb", action="client")))
        elif i == "bypass": son = 1

    if callback_query["language"] == "uzb":
        if client and client[0][0] is not None:
            markup.add(InlineKeyboardButton(text="📥 Savat", callback_data=vote_cb.new(stage="start_arr", id="start", name="basket", number="", language="uzb", action="client")))
        if son == 1:markup.add(InlineKeyboardButton(text="Barcha modellarga ↪️",callback_data=vote_cb.new(stage="name", id="plus", name="bypass", number="", language=callback_query["language"], action="client")))
        await bot.send_message(message.from_user.id, "Qaysi turdagi mashinani extiyot qisimi kerak 🙃", reply_markup=markup)

    elif callback_query["language"] == "rus":
        if client and client[0][0] is not None:
            markup.add(InlineKeyboardButton(text="📥 Корзина",callback_data=vote_cb.new(stage="start_arr", id="start", name="basket",number="None", language="rus", action="client")))
        await bot.send_message(message.from_user.id, "Для какого типа машины нужна запчасть 🙃", reply_markup=markup)
    elif callback_query["language"] == "eng":
        if client and client[0][0] is not None:
            markup.add(InlineKeyboardButton(text="📥 Basket", callback_data=vote_cb.new(stage="start_arr", id="start", name="basket", number="", language="eng", action="client")))
        await bot.send_message(message.from_user.id, "What type of machine do you need a spare part for? 🙃",reply_markup=markup)
    if client: conn.execute(f"update CLIENT_ set corporation = '{callback_query['name']}' where id = (?);",(message.from_user.id,))
    else: conn.execute("insert into CLIENT_(id,corporation) values (?,?);",(message.from_user.id,callback_query["name"]))


async def client_name_bypass(message:types.Message,conn,vote_cb,callback_query):
    client = conn.execute("select corporation from car where id = (?);",(message.from_user.id,)).fetchall()[0]
    callback_query["name"] = conn.execute("select id from CAR where corporation = (?) and name = 'bypass';",(client[0],)).fetchall()[0][0]
    await client_print_car(message,conn, vote_cb, callback_query)