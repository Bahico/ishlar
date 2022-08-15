from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from bot.menu.main_menu import bot_main_menu
from branch.menu.main_menu import admin_branch_menu
from ..car_arr.car_corporation import client_car_corporation
from ..car_arr.car_name import client_car_name

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_start(message: types.Message, conn, vote_cb):
    branch = conn.execute("select language, branch from ADMIN where id = (?) and test = 4;", (message.from_user.id,)).fetchall()
    client = conn.execute("select language from CLIENT where id = (?);", (message.from_user.id,)).fetchall()
    I_ = conn.execute("select language from I_ where id = (?) and test = 4;",(message.from_user.id,)).fetchall()
    if I_:
        await bot_main_menu(message,vote_cb,I_[0][0],conn)
    elif branch:
        await admin_branch_menu(message,conn,vote_cb,branch[0][0])
    elif not client:
        markup = InlineKeyboardMarkup(resize_keyboard=True)
        markup.row_width = 2
        markup.row(
            InlineKeyboardButton(text="🇺🇿 O'zbekcha",
                                 callback_data=vote_cb.new(stage="start", id="start", name="None", number="None", language="uzb", action="client")),
            InlineKeyboardButton(text="🇬🇧 English",
                                 callback_data=vote_cb.new(stage="start", id="start", name="None", number="None", language="eng", action="client")),
            InlineKeyboardButton(text="🇷🇺 Русский",
                                 callback_data=vote_cb.new(stage="start", id="start", name="None", number="None", language="rus", action="client"))
        )
        await bot.send_message(message.from_user.id, "Tilni tanlang 😊\nSelect a language 😊\nВыберите язык 😊",reply_markup=markup)
    elif client:
        await client_car_corporation(message,conn,vote_cb,client[0][0])
