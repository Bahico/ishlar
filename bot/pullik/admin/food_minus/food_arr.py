from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

# some code

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def get_arr(message: types.Message, conn, vote_cb, callback_query):
    food = conn.execute(f"select {callback_query['text']} from BRANCH where id = (?);",(callback_query["branch"]),).fetchall()
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    food = food[0]
    food = food[0].split(".")
    son = 0
    for i in food:
        son = 1
        i = i.split(',')
        markup.add(InlineKeyboardButton(text=i[1],callback_data=vote_cb.new(location=callback_query["text"], text=i[1], branch=callback_query["branch"], language="uzb", action="admin")))
    if son == 1:
        await bot.send_message(message.from_user.id,"Qaysi turdagi maxsulotni o'chirish kerak?",reply_markup=markup)
    else:
        await bot.send_message(message.from_user.id,"Bu turdagi maxsulotlarni hammasi o'chirilgan.")