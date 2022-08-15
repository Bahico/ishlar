from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

from bot.menu.main_menu import bot_main_menu

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def bot_language(message: types.Message, conn, vote_cb, callback_query):
    await bot_main_menu(message, vote_cb, callback_query["language"], conn)
