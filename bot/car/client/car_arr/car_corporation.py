from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_car_corporation(message:types.Message,conn,vote_cb, language):
    """

    :param language:
    :param message:
    :param conn:
    :param vote_cb:
    :return:
    """
    try:
        await bot.delete_message(message.from_user.id,message.message_id+1)
    except:
        pass
    client = conn.execute("select basket from CLIENT_ where id = (?);", (message.from_user.id,)).fetchall()
    car = conn.execute("select name, id from brand;").fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 3
    for i in car:
        markup.insert(InlineKeyboardButton(text=i[0], callback_data=vote_cb.new(stage="start_arr", id="start", name=i[1], number="None", language="uzb", action="client")))
    if language == "uzb":
        if client and client[0][0] is not None:
            markup.add(InlineKeyboardButton(text="📥 Savat", callback_data=vote_cb.new(stage="start_arr", id="start", name="basket", number="None", language="uzb", action="client")))
        await bot.send_message(message.from_user.id, "Qaysi turdagi mashinani extiyot qisimi kerak 🙃", reply_markup=markup)

    elif language == "rus":
        if client and client[0][0] is not None:
            markup.add(InlineKeyboardButton(text="📥 Корзина",callback_data=vote_cb.new(stage="start_arr", id="start", name="basket",number="None", language="rus", action="client")))
        await bot.send_message(message.from_user.id, "Для какого типа машины нужна запчасть 🙃", reply_markup=markup)
    elif language == "eng":
        if client and client[0][0] is not None:
            markup.add(InlineKeyboardButton(text="📥 Basket", callback_data=vote_cb.new(stage="start_arr", id="start", name="basket", number="None", language="eng", action="client")))
        await bot.send_message(message.from_user.id, "What type of machine do you need a spare part for? 🙃",reply_markup=markup)
