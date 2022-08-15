import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

from bot.callback import get_bot_callback
from bot.start import bot_start
from client.callback.callback import client_client_callback
from client.start.start import client_start
from branch.start.start import admin_start_admin
from branch.callback.callback import admin_branch_callback
from contact import get_contact
from location import get_location
from logout import get_logout_message

from config import TOKEN
from menu import get_menu
from message import get_message_all
from photo import get_photo

conn = sqlite3.connect('sqlite.db')

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

vote_cb = CallbackData("vote", "stage", "id", "name", "number", "language", "action")


@dp.message_handler(commands=['start'])
async def get_start_(message: types.Message):
    await client_start(message, conn, vote_cb)
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(commands=['branch'])
async def get_branch(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await admin_start_admin(message, conn, vote_cb)


@dp.message_handler(commands=['bot'])
async def get_bot(message: types.Message):
    await bot_start(message, conn)
    await message.delete()


@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    await get_contact(message, conn, vote_cb)
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(content_types=['location'])
async def location(message: types.Message):
    await get_location(message, conn, vote_cb)
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(commands=['logout'])
async def get_logout(message: types.Message):
    await get_logout_message(message, conn)
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await get_menu(message, conn, vote_cb)


@dp.callback_query_handler(vote_cb.filter(action="client"))
async def get_admin(message: types.Message, callback_data: dict):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await client_client_callback(message, conn, vote_cb, callback_data)


@dp.callback_query_handler(vote_cb.filter(action="bot"))
async def get_admin(message: types.Message, callback_data: dict):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await get_bot_callback(message, conn, vote_cb, callback_data)


@dp.callback_query_handler(vote_cb.filter(action="branch"))
async def get_admin(message: types.Message, callback_data: dict):
    try:
        await bot.delete_message(message.from_user.id, message.message.message_id)
    except:
        pass
    await admin_branch_callback(message, conn, vote_cb, callback_data)


@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    await get_photo(message, conn, vote_cb)


@dp.message_handler()
async def get_message(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await get_message_all(message, conn, vote_cb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
