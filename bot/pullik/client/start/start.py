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
    markup.add(KeyboardButton(text="๐ท๐บ Pัััะบะธะน"))
    markup.add(KeyboardButton(text="๐บ๐ฟ O'zbekcha"))
    markup.add(KeyboardButton(text="๐ฌ๐ง English"))
    await bot.send_message(message.from_user.id,"Assalomu aleykum {0.first_name}\n\nTilni tanlang!๐๐".format(message.from_user),reply_markup=markup)
