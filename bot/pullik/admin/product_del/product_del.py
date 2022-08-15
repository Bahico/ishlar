from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# 'location', 'text', 'branch', 'language', 'action'
# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_product(message: types.Message, conn, vote_cb):
    person = conn.execute("select branch from ADMIN where id = (?);",(message.from_user.id,)).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True).row(
            InlineKeyboardButton(text="🧇 Vaflilar",callback_data=vote_cb.new(location='--', text='waffle', branch=person[0][0], language="uzb", action="admin")),
            InlineKeyboardButton(text="🧃 Salqin ichimliklar",callback_data=vote_cb.new(location='--', text='drinks', branch=person[0][0], language="uzb", action="admin")),
            InlineKeyboardButton(text="☕️ Coffee",callback_data=vote_cb.new(location='--', text='coffee', branch=person[0][0], language="uzb", action="admin")),
            InlineKeyboardButton(text="🍔️ Fast Food",callback_data=vote_cb.new(location='--', text='fast_food', branch=person[0][0], language="uzb", action="admin"))
        )
    await bot.send_message(message.from_user.id,"Menudan tanlang",reply_markup=markup)
