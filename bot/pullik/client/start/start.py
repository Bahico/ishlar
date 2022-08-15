from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def get_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text="🇷🇺 Pусский"))
    markup.add(KeyboardButton(text="🇺🇿 O'zbekcha"))
    markup.add(KeyboardButton(text="🇬🇧 English"))
    await bot.send_message(message.from_user.id,"Assalomu aleykum {0.first_name}\n\nTilni tanlang!👇👇".format(message.from_user),reply_markup=markup)
