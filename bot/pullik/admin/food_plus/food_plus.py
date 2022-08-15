from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_food_plus(message: types.Message, vote_cb, callback_query):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(InlineKeyboardButton(text="🧇 Vaflilar",callback_data=vote_cb.new(location='+', text='waffle', branch=callback_query["branch"], language="uzb", action="admin")))
    markup.add(InlineKeyboardButton(text="🧃 Salqin ichimliklar",callback_data=vote_cb.new(location='+', text='drinks', branch=callback_query["branch"], language="uzb", action="admin")))
    markup.add(InlineKeyboardButton(text="☕️ Coffee",callback_data=vote_cb.new(location='+', text='coffee', branch=callback_query["branch"], language="uzb", action="admin")))
    markup.add(InlineKeyboardButton(text="🍔️ Fast Food",callback_data=vote_cb.new(location='+', text='fast_food', branch=callback_query["branch"], language="uzb", action="admin")))
    markup.add(InlineKeyboardButton(text="⬅️ Ortga",callback_data=vote_cb.new(location='+', text='back', branch=callback_query["branch"], language="uzb", action="admin")))
    await bot.send_message(message.from_user.id,"Menu",reply_markup=markup)