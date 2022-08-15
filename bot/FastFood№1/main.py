import sqlite3

from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentTypes
from aiogram.utils import executor

import consumer

BOT_TOKEN = '5076362804:AAE5EGEkcF2-Wulbn--qhBOTxSrFX_LLiYA'


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def get_start(message: types.Message):
    await consumer.consumer_start.get_start(message)

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)