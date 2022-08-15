import sqlite3

import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def user_about(message: types.Message, vote_cb: aiogram.utils.callback_data.CallbackData):
    markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text="⬅️ORTGA", callback_data=vote_cb.new(rol="user", stage="",  stage1="", tur="")))
    await bot.send_message(message.from_user.id, "pass", reply_markup=markup)
