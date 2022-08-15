# import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

from admin.callback import admin_callback
from admin.start import admin_start
from config import TOKEN
from message import main_message

# from user.callback import user_callback
# from user.start.start import user_start

# logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

vote_cb = CallbackData("vote", "rol", "stage", "stage1", "tur")

main_conn = sqlite3.connect("dp.db")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await admin_start(message, main_conn, vote_cb)


# @dp.message_handler(commands=['admin'])
# async def admin(message: types.Message):
#     await admin_start(message, main_conn)


# @dp.callback_query_handler(vote_cb.filter(rol="user"))
# async def user(message: types.Message, callback_data: dict):
#     await bot.delete_message(message.from_user.id, message.message.message_id)
#     await user_callback(message, vote_cb, main_conn, callback_data)
#     main_conn.commit()


@dp.callback_query_handler(vote_cb.filter(rol="admin"))
async def admin_(message: types.Message, callback_data: dict):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await admin_callback(message, vote_cb, main_conn, callback_data)
    main_conn.commit()


@dp.message_handler()
async def message_(message: types.Message):
    await message.delete()
    await main_message(message, main_conn, vote_cb)
    main_conn.commit()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
