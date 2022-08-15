from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

# some code

# "stage", "id", "name", "number", "language", "action"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def admin_branch_location(message:types.Message,conn,callback_query):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    conn.execute("update ADMIN set settings = 'branch_location' where id = (?);",(message.from_user.id,))
    if callback_query["language"] == "uzb":
        markup.add(KeyboardButton("🗺 Filial joylashuvi",request_location=True))
        await bot.send_message(message.from_user.id,"Filial joylashgan joyni kiriting.",reply_markup=markup)
    elif callback_query["language"] == "eng":
        markup.add(KeyboardButton("🗺 Filial joylashuvi",request_location=True))
        await bot.send_message(message.from_user.id,"Filial joylashgan joyni kiriting.",reply_markup=markup)
    elif callback_query["language"] == "rus":
        markup.add(KeyboardButton("🗺 Filial joylashuvi",request_location=True))
        await bot.send_message(message.from_user.id,"Filial joylashgan joyni kiriting.",reply_markup=markup)