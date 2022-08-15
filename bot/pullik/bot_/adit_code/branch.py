from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

delivery_edit = None
food_edit = None


async def get_edit(message: types.Message, conn, vote_cb):
    branch = conn.execute("select id, name from BRANCH;").fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    for i in branch:
        markup.add(
            InlineKeyboardButton(text=i[1], callback_data=vote_cb.new(location="branch", text="edit", branch=i[0],
                                                                      language="uzb", action="bot_")))
    await bot.send_message(message.from_user.id, "Qaysi filialni kodini o'zgartirmoqchisiz.",reply_markup=markup)


async def get_delivery_food(message: types.Message, conn, vote_cb, id):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row(
        InlineKeyboardButton(text="Maxsulotga javob beruvchi",
                             callback_data=vote_cb.new(location="food", text="edit", branch=id,
                                                       language="uzb", action="bot_")),
        InlineKeyboardButton(text="Buyurtma qabul qiluvchi",
                             callback_data=vote_cb.new(location="delivery", text="edit", branch=id,
                                                       language="uzb", action="bot_"))
    )
    await bot.send_message(message.from_user.id,"Qanday admin kodini o'zgartirmoqchisiz.",reply_markup=markup)


async def get_delivery_edit(message: types.Message, id):
    global delivery_edit
    delivery_edit = id
    await bot.send_message(message.from_user.id, "Yangi kod kiriting: ")


async def get_food_edit(message: types.Message, id):
    global food_edit
    food_edit = id
    await bot.send_message(message.from_user.id, "Yangi kod kiriting: ")


def get_none_():
    global food_edit, delivery_edit
    food_edit = None
    delivery_edit = None
