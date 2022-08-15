from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def client_print_car(message: types.Message, conn, vote_cb, callback_query):
    markup = InlineKeyboardMarkup(reply_markup=True)
    if callback_query["language"] == "uzb":
        print(callback_query["name"],callback_query["language"],)
        markup.row(InlineKeyboardButton(text="⚒ Kuzov", callback_data=vote_cb.new(stage="kuzif", id="start",name=str(callback_query["name"]), number="", language=callback_query["language"], action="client")),
                   InlineKeyboardButton(text="⚙️ Mator", callback_data=vote_cb.new(stage="mator", id="start",name=str(callback_query["name"]), number="", language=callback_query["language"],action="client")),
                   InlineKeyboardButton(text="💈 Tuning",callback_data=vote_cb.new(stage="tuning", id="start", name=str(callback_query["name"]), number="", language=callback_query["language"],action="client")))
        await bot.send_message(message.from_user.id,"pass",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.row(InlineKeyboardButton(text="⚒ Кузов", callback_data=vote_cb.new(stage="kuzif", id="start",name=callback_query["name"], number="", language=callback_query["language"], action="client")),
                   InlineKeyboardButton(text="⚙️ Матор", callback_data=vote_cb.new(stage="mator", id="start",name=callback_query["name"], number="", language=callback_query["language"],action="client")),
                   InlineKeyboardButton(text="💈 Тюнинг",callback_data=vote_cb.new(stage="tuning", id="start", name=callback_query["name"], number="", language=callback_query["language"],action="client")))
        await bot.send_message(message.from_user.id,"pass",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.row(InlineKeyboardButton(text="⚒ Kuzov", callback_data=vote_cb.new(stage="kuzif", id="start",name=callback_query["name"], number="", language=callback_query["language"], action="client")),
                   InlineKeyboardButton(text="⚙️ Mator", callback_data=vote_cb.new(stage="mator", id="start",name=callback_query["name"], number="", language=callback_query["language"],action="client")),
                   InlineKeyboardButton(text="💈 Tuning",callback_data=vote_cb.new(stage="tuning", id="start", name=callback_query["name"],  number="", language=callback_query["language"],action="client")))
        await bot.send_message(message.from_user.id,"pass",reply_markup=markup)

    conn.execute(f"update CLIENT_ set spare = '{callback_query['name']}', corporation = Null, name = Null, number = NULL, paditsiya = NULL where id = (?);",(message.from_user.id,))
