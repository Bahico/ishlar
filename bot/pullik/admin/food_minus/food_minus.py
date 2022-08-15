from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_food_minus(message: types.Message, conn, vote_cb, callback_query, branch):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    son_ = 0
    if branch[1] is not None:
        son_ = 1
        markup.add(InlineKeyboardButton(text="🧇 Vaflilar",callback_data=vote_cb.new(location='-', text='waffle', branch=callback_query["branch"], language="uzb", action="admin")))
    if branch[3] is not None:
        son_ = 0
        markup.add(InlineKeyboardButton(text="🧃 Salqin ichimliklar",callback_data=vote_cb.new(location='-', text='drinks', branch=callback_query["branch"], language="uzb", action="admin")))
    if branch[2] is not None:
        son_ = 1
        markup.add(InlineKeyboardButton(text="☕️ Coffee",callback_data=vote_cb.new(location='-', text='coffee', branch=callback_query["branch"], language="uzb", action="admin")))
    if branch[0] is not None:
        son_ = 1
        markup.add(InlineKeyboardButton(text="🍔️ Fast Food",callback_data=vote_cb.new(location='-', text='fast_food', branch=callback_query["branch"], language="uzb", action="admin")))
    if son_ == 1:
        await bot.send_message(message.from_user.id,"O'chiriladigan maxsulot menusi.",reply_markup=markup)
    else:
        await bot.send_message(message.from_user.id,"Hali maxsulot qo'shilmagan")
